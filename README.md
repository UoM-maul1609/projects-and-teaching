# Projects and Teaching
This repository describes how to set-up your system to run many of the numerical models at [https://github.com/UoM-maul1609](https://github.com/UoM-maul1609).

In order to run the models easily on your computer you can install a program called [Docker Desktop](https://www.docker.com/products/docker-desktop/). Docker Desktop allows you to run applications in a standardized environment using a so-called container. Think of it as a virtual environment that contains everything you need to be able to run the code. 

Why not just run the code on my computer without Docker Desktop? There are two main reasons for the models used at [https://github.com/UoM-maul1609](https://github.com/UoM-maul1609). 

Firstly, for models that are written in Python, you would need to install Python and all the necessary libraries. This can be a pain at times. Using a Docker container we are able to ship Python and all the necessary libraries we need to run the python code.  

Secondly, for models that are written in Fortran, you would need to install a Fortran compiler, NetCDF libraries and MPI libraries and then compile the model for your system. This can also be a pain. Using a Docker container we can also ship all the necessary compilers, libraries and other tools to enable you to easily get up to speed. 