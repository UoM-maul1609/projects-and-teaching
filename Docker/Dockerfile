# syntax=docker/dockerfile:1
FROM ubuntu:22.04


# install app dependencies
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y ipython3 \
	shotwell x11-apps gfortran libnetcdff-dev mpich git make bash-completion \
	python3-netcdf4 gedit python3-matplotlib vim nano python3-tqdm texlive \
	dvipng texlive-latex-extra texlive-base texlive cm-super 

#RUN git clone https://github.com/UoM-maul1609/bin-microphysics-model
#RUN git clone https://github.com/UoM-maul1609/dynamical-cloud-model
RUN /bin/bash
WORKDIR ./home

#RUN make NETCDFLIB=-L/usr/lib/x86_64-linux-gnu/ NETCDFMOD=/usr/include/ FFLAGS='-O2 -w -o' FFLAGS2='-O2 -w -o' FFLAGSOMP='-O2 -w -o'

# app is installed

