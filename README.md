# Projects and Teaching
This repository describes how to set-up your system to run many of the numerical models at [https://github.com/UoM-maul1609](https://github.com/UoM-maul1609).

In order to run the models easily on your computer you can install a program called [Docker Desktop](https://www.docker.com/products/docker-desktop/). Docker Desktop allows you to run applications in a standardized environment using a so-called container. Think of it as a virtual environment that contains everything you need to be able to run the code. 

Why not just run the code on my computer without Docker Desktop? There are two main reasons for the models used at [https://github.com/UoM-maul1609](https://github.com/UoM-maul1609). 

Firstly, for models that are written in Python, you would need to install Python and all the necessary libraries. This can be a pain at times. Using a Docker container we are able to ship Python and all the necessary libraries we need to run the python code.  

Secondly, for models that are written in Fortran, you would need to install a Fortran compiler, NetCDF libraries and MPI libraries and then compile the model for your system. This can also be a pain. Using a Docker container we can also ship all the necessary compilers, libraries and other tools to enable you to easily get up to speed. 

# Other software to install



# Downloading the container from GHCR
I have included a container image as a package with this repository. 


Once you have downloaded the container you should not need to do this again, unless you wish to start from scratch. 

# Example taught module
See the example

# Example projects
See the example


# Notes for admins
If interested you may build your own container image from the Dockerfile in this repository. First run Docker Desktop and, from the commandline, change directory to Docker/ and build the docker file

    cd Docker
    docker build -t project-and-teaching .
    
This will build the docker container image from the definitions in the Dockerfile, which you can deploy at test as follows. If on a mac type this first

    xhost +

Then type

    docker run -it --rm -e DISPLAY=host.docker.internal:0 -v /tmp/.x11-unix:/tmp/.x11-unix  project-and-teaching
    
The above line runs the docker image. The -it flag means run interactively, so we can interact with the shell and project-and-teaching is the name of the docker image. The display is exported to you local computer so you can open up windows (e.g. text editors).