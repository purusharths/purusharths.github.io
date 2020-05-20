---
layout: post
title: "Making RPM packages @ fedoraproject.org"
categories: misc
---

There are great many tutorials out there for packaging. The RPM docs are meticuliously written covering all the details and error logs. I'm using this blogpost as my own personal scratchpad which I can rerfer to whenever needed.



### CMake Installations

- Check in the build logs if the flags set in the CMake file are present in `rpm -E %{optflags}` 
```
-O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions 
-fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/
redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection
```
	* These are the flags that Fedora sets for packages, and *only* these must be set

	* Check where in the CMakeLists.txt files upstream had hardcoded their flags: [Fedora Default Compiler Flags](https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags)

	* PS: it isn't forbidden to use other flags, but unless there's a very good reason to do so, we stick to these. If for some reasons upstream package is not compiling without the hard-coded flags, we'd have to work with upstream to see why removing their flags breaks the compilation; and, if necessary we add them to the default set.
	However, the default flags are general enough and rarely cause such issues

	* EXAMPLE: For tpcclib upstream used `-s`, which strips the binaries. Stripped binaries don't generate debuginfo

	* To search for the instance where different flags are used, search for general tokens like: `FLAGS/CFLAGS/CXXFLAGS` 
	
	* CMakeList files are unique for each project. They'll use `cmake` directives, but apart from that they're like code

- About "build" tools <br>
	* There are many different "build" tools, `configure` is only used for "Autotools". 
A `CMakeLists.txt` uses the cmake system. Make changes in %build as per the `cmake` guideline page

	* When you're in the build directory, you'll have to use `%cmake ..` Eg:
```
%install
  pushd build
    %cmake ..
    %make_install
  popd build
```

- Avoid Static Files/library 
(More on this later)

	* All .a files are a static library and are generally avoided: [https://docs.fedoraproject.org/en-US/packaging-guidelines/#packaging-static-libraries](https://docs.fedoraproject.org/en-US/packaging-guidelines/#packaging-static-libraries)

- GCC Issues
	* Ensure that the compilation flags are compatible with the current version of GCC (use `man gcc`)
		* [https://gcc.gnu.org/gcc-10/porting_to.html](https://gcc.gnu.org/gcc-10/porting_to.html)
		* [https://gcc.gnu.org/onlinedocs/gcc/Attribute-Syntax.html](https://gcc.gnu.org/gcc-10/porting_to.html)
- Stay Close to the Upstream
	* [https://fedoraproject.org/wiki/Staying_close_to_upstream_projects](https://fedoraproject.org/wiki/Staying_close_to_upstream_projects)
	

	set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}" CACHE PATH "Default install path" FORCE) is present in CMAKELists.txt by default. my path removed the line. So this patch can be removed?

- Use `git-format-patch` for generating patches
	* Download the tar.gz from the repo remote
	* Initialize git repo
	* Do a `git checkout -b <branch-name>`
	* Make changes and commit (DO NOT MERGE TO `master`)
	* Switch back to master and;
	* `git format-patch <branch-name>`
	* Patch files will be created based on each commit in the `<branch-name>`


- Header files not found:
	* If the build is failing in few of the arches and the buildlog points to `*.h - not found` error, then there could be a mis-configuration with the default flags. For instance:
```
-- Looking for include file stdint.h
-- Looking for include file stdint.h - not found
```
	* In this case, `-msse2` flag is being set on a 32-bit compiler. However, GCC ARM Options suggest otherwise.
	> "For the x86-32 compiler, you must use -march=cpu-type, -msse or -msse2 switches to enable SSE extensions and make this option effective. For the x86-64 compiler, these extensions are enabled by default."
	
	* That is, `-msse2` is *not* a valid option for arm: [https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html](https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html).
	Therefore, when the upstream set -msse2 for *all* 32bit systems, they broke the 32bit arm builds

- Issues with path
 	* If the  upstream defines LIBPATH to be a relative path: "lib" (`DESTINATION ${LIBPATH}`) - for example if they want to install the package locally instead of at the system directories.
	* If you run `rpm -E %cmake`, you'll see that the macro defines the standard library path for us in LIB_INSTALL_DIR, so simpler to just use that
	* To apply the fix in all the nested `CmakeLists.txt` files use:
	```
	find . -name "CMakeLists.txt" -exec sed -i 's/LIBPATH/LIB_INSTALL_DIR/g' '{}' \;
	```
	or
	```
	find . -type f -name "CMakeLists.txt" -print0 | xargs -0 sed -i'' -e 's/DESTINATION ${LIBPATH}/DESTINATION ${INCLUDE_INSTALL_DIR}/g'
	```


### Devel Files
> More on these later

### Tools used
- Koji
- rpmbuild
- fedora-review
- mock

### Relevant Links
[https://fedoraproject.org/wiki/How_to_create_a_GNU_Hello_RPM_package](https://fedoraproject.org/wiki/How_to_create_a_GNU_Hello_RPM_package) <br>
[http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html](http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html) <br>
[https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses](https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses)<br>
[https://fedoramagazine.org/how-rpm-packages-are-made-the-spec-file/](https://fedoramagazine.org/how-rpm-packages-are-made-the-spec-file/)<br>
[https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/](https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/)<br>
[https://rpm.org/user_doc/autosetup.html](https://rpm.org/user_doc/autosetup.html)<br>
[https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch09s05s07.html](https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch09s05s07.html)<br>
[https://fedoraproject.org/wiki/Join_the_package_collection_maintainers](https://fedoraproject.org/wiki/Join_the_package_collection_maintainers)<br>
[https://apps.fedoraproject.org/packages/](https://apps.fedoraproject.org/packages/)
[FHS](http://www.pathname.com/fhs/pub/fhs-2.3.html)<br>
[Config Macros](http://ftp.rpm.org/api/4.4.2.2/config_macros.html)<br>
[Devel Packages](https://docs.fedoraproject.org/en-US/packaging-guidelines/#_devel_packages)<br>
[Compile Flags](https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags)<br>
[Useless or incomplete debuginfo packages due to packaging issues](https://fedoraproject.org/wiki/Packaging:Debuginfo#Useless_or_incomplete_debuginfo_packages_due_to_packaging_issues)<br>
[Filesystem Layout](https://docs.fedoraproject.org/en-US/packaging-guidelines/#_filesystem_layout)<br>
[Versioning](https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/)<br>
[Snapshots](https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/#_snapshots)