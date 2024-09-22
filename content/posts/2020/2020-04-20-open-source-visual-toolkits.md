---
title: "Directory of Open Source Visualization Toolkits"
date: 2020-01-15 10:59
summary: A not so maintained list for setting up quick and dirty setup for visualizations pipeline. Some are only for visualization which has been generated already, while some are a complete package.
Tags: 
  - open-source
  - visualization
---

- ### PyVTK 
	* PyVTK is the wrapper for VTK (written in C++). VTK or visualization Toolkit is a high-level visualization library used for 3D computer graphics and visualizations.
		* Maintained and developed by: [Kitware](https://www.kitware.com/)

- ### Manim (Mathematical Animation)
	* Started by Grant Sanderson (aka 3b1b) for as his own personal project. Now one of the most famous toolkits out there for explanatory animations. It uses `cairo (pycairo)` to write svgs and `ffmpeg` to merge them. The final output is a `.mp4` file.
	However, the lack of documentation makes it harder to use. 
		* [Github](https://github.com/3b1b/manim)

- ### Mayavi
	* Created by [Prof. Prabhu Ramachandran](https://www.aero.iitb.ac.in/~prabhu/), mayavi works on top of VTK. It can either be used as a python package or from the GUI module. More info avilable at the [Mayavi docs](http://docs.enthought.com/mayavi/mayavi/overview.html#what-is-mayavi2)
		* Mayavi is now under the Enthought suite of scientific Python programs<br>
	[Github](https://github.com/enthought/mayavi) |  [Tutorial](https://www.youtube.com/watch?v=r6OD07Qq2mw)

- ### Vispy
	* VisPy was designed by Luke Campagnola, Almar Klein, Cyrille Rossant and Nicolas P. Rougier. It was aimed at creating fast andscalable visualization. VisPy is a sucessor of [visvis](https://github.com/almarklein/visvis). However, I am doubful if the project is being actively maintained.<br>
	[Home](http://vispy.org/) | [GitHub](https://github.com/vispy/vispy) | [Documentation](http://vispy.org/documentation.html)

- ### Glumpy
	* VisPy's sister project, glumpy is a neatly designed interface between NumPy and OpenGL. It gives more low-level access than VisPy. Their documentation states: "_Glumpy is a python library for scientific visualization that is both fast, scalable and beautiful. Glumpy offers an intuitive interface between numpy and modern OpenGL._"<br>
	[GitHub](https://github.com/glumpy/glumpy) | [Documentation](https://glumpy.readthedocs.io/en/latest/)