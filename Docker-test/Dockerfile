# syntax=docker/dockerfile:1
FROM ubuntu:latest


# install app dependencies
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y ipython3 \
	shotwell x11-apps gfortran libnetcdff-dev mpich git make bash-completion \
	python3-netcdf4 gedit python3-matplotlib vim nano python3-tqdm texlive \
	dvipng texlive-latex-extra texlive-base texlive cm-super imagemagick tkdiff \
	openssh-server python3-pip sudo openssh-server systemctl ffmpeg htop

#RUN git clone https://github.com/UoM-maul1609/bin-microphysics-model
#RUN git clone https://github.com/UoM-maul1609/dynamical-cloud-model
RUN /bin/bash
WORKDIR /root
ENV USER=root
RUN apt-get install -y libgeos-dev
RUN pip3 install basemap --user


RUN systemctl enable ssh
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo 'root:root123' |chpasswd
RUN service ssh start
ENTRYPOINT service ssh restart && bash



#RUN make NETCDFLIB=-L/usr/lib/x86_64-linux-gnu/ NETCDFMOD=/usr/include/ FFLAGS='-O2 -w -o' FFLAGS2='-O2 -w -o' FFLAGSOMP='-O2 -w -o'

# app is installed
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]

