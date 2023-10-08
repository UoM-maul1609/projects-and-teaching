# Projects and Teaching
This repository describes how to set-up your system to run many of the numerical models at [https://github.com/UoM-maul1609](https://github.com/UoM-maul1609).

In order to run the models easily on your computer you can install a program called [Docker Desktop](https://www.docker.com/products/docker-desktop/). Docker Desktop allows you to run applications in a standardized environment using a so-called container. Think of it as a virtual environment that contains everything you need to be able to run the code. 

Why not just run the code on my computer without Docker Desktop? There are two main reasons for the models used at [https://github.com/UoM-maul1609](https://github.com/UoM-maul1609). 

Firstly, for models that are written in Python, you would need to install Python and all the necessary libraries. This can be a pain at times. Using a Docker container we are able to ship Python and all the necessary libraries we need to run the python code.  

Secondly, for models that are written in Fortran, you would need to install a Fortran compiler, NetCDF libraries and MPI libraries and then compile the model for your system. This can also be a pain. Using a Docker container we can also ship all the necessary compilers, libraries and other tools to enable you to easily get up to speed. 

# Other software to install

If you are running windows you may find it useful to install [git for Windows](https://gitforwindows.org). This enables you to download code repositories from Github using the command line so it is quite useful. Git is already installed by default on most Macs, so additional software is not needed. 

On a Chromebook you should first install the linux developer tools.

On Mac, Windows or Chromebook open a terminal or Git-CMD window and then download this git repository by typing
	
	git clone https://github.com/UoM-maul1609/projects-and-teaching
	
On the Chromebook you do not install Docker Desktop, but you install Docker by typing 
	
	./projects-and-teaching/scripts/set-up-chromebook-docker.sh
	
# Downloading / running the container from GHCR
I have included a container image as a package with this repository. You need to make sure that Docker Desktop is running (if on Mac or Windows). 

Assuming you have downloaded this git repository, you can then download and run the container by typing the following.

Mac:

	./projects-and-teaching/scripts/docker-run-mac.sh
Chromebook:

	./projects-and-teaching/scripts/docker-run-chromeos.sh
Windows: 
	
	.\projects-and-teaching\scripts\docker-run-win.bat


# Example taught module
See the example

# Projects
Here are details of projects:
 
1. [Single Column Modelling](scm-modelling/)
2. [Secondary Ice Modelling](parcel-modelling/)
3. [Saturn's Hexagon](saturn-hexagon-modelling/)
4. [Marine Cloud Brightening](mcb-modelling/)

# Notes for admins
If interested you may build your own container image from the Dockerfile in this repository. First run Docker Desktop and, from the commandline, make sure you are in the folder of this repository, and build the docker file

    docker build -t project-and-teaching-all .
    
This will build the docker container image from the definitions in the Dockerfile, which you can deploy at test as follows. If on a mac type this first

    xhost +

Then type

    docker run -it --rm -e DISPLAY=host.docker.internal:0 -v /tmp/.x11-unix:/tmp/.x11-unix  project-and-teaching-all
    
The above line runs the docker image. The -it flag means run interactively, so we can interact with the shell and project-and-teaching is the name of the docker image. The display is exported to you local computer so you can open up windows (e.g. text editors).