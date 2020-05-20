---
layout: post
title: "Linux from scratch (and what I learnt form it)"
categories: linux
---

I got a spare system during the last days 2018 and decided to try my hands at it. The process was, suprisingly, not as complicated as one would expect. Infact it was quite straightforward. The intial housekeeping steps were a bit discouraging but once the user and group for `lfs` were set up, things became a lot easier (and repetitive).

Most of the time (while `Constructing a Temporary System`), I had to use variations of the following command:
```
mkdir -v build
cd build
../configure <tool-specific-flags>
make -j8 
make install
```
To be fair, a good amount of time went in studying about the config parameters for different tools like GCC, Bash etc. 
```
[UPDATE] This process was especially helpful for me while Packaging @ Fedora
```
The process was so repetitive that I thought of writing a bash script for it, but as it turns out, folks at [linuxfromscratch.org](http://www.linuxfromscratch.org/alfs/index.html) already anticipated this.

Things took an upwards turn from chapter 7 of the LFS book (System Configuration). Everything that followed is captivating at the least. (See takeaway section below)

**Tl;dr:** The process was interesting; but tedious at times. configuration options are important. Things get a lot more interesting from Chapter 7 onwards.

#### My Takeaway from the process: install arch first
I say this because if you play your cards right, you'd get to pick up the arch installation right from System Configuration section of LFS, which -- atleast in my views -- is the most important section of the entire process. 

--

The whole process took me a couple of days iirc. Thankfully, the spare machine that I recieved was an old i7 ThinkPad while made the whole thing quite enjoyble. If you're planning on doing it over a VM, then be prepared to leave the system overnight for compilation.