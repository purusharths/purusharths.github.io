---
layout: post
title: "Installing manim "
categories: fossee
---

Manim installation has become quite straghtforward since the `manimlib` wheel was released on `pip`.
The system dependencies are as follows:
1. `cario`: 2D graphics library
2. `latex`: A high-quality typesetting system
3. `ffmpeg`: Rendering videos
4. `sox`: Sound Processing

## Installing System Dependencies

- Fedora
	```
	sudo dnf install cairo-devel ffmpeg sox texlive-scheme-full
	```
- Ubuntu
	```
	sudo apt install libcairo2-dev ffmpeg sox texlive texlive-fonts-extra texlive-latex-extra texlive-latex-recommended texlive-science tipa
	```

Additionally make sure that python 3.7.x is installed, along with the header/static files, venv and pip
```
sudo apt install python3-dev python3-venv python3-pip
```

## Installing manimlib

1. Create the virtual environment: `python3 -m venv ~/manim-venv`
2. Activate the environment: `source ~/manim-venv/bin/activate`
3. pip installation: `pip install manimlib`
4. Check your installation by using the following commands:
```
wget https://static.fossee.in/animations/workshop/manim_hello_world_text.py 
manim manim_hello_world_text.py TestManimInstallation 
```