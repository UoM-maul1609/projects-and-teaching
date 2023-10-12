# syntax=docker/dockerfile:1
FROM ubuntu:latest


# install app dependencies
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y ipython3 \
	shotwell x11-apps gfortran libnetcdff-dev mpich git make bash-completion \
	python3-netcdf4 gedit python3-matplotlib vim nano python3-tqdm texlive \
	dvipng texlive-latex-extra texlive-base texlive cm-super imagemagick tkdiff \
	openssh-server python3-pip sudo openssh-server systemctl ffmpeg htop \
	python3-pandas

#RUN git clone https://github.com/UoM-maul1609/bin-microphysics-model
#RUN git clone https://github.com/UoM-maul1609/dynamical-cloud-model
RUN /bin/bash
WORKDIR /root
ENV USER=root
RUN apt-get install -y libgeos-dev
RUN pip3 install basemap --user


RUN systemctl enable ssh
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo 'root:root$123xyz!@' |chpasswd

# SET UP SOME USERS
RUN useradd -ms /bin/bash mpec01
RUN useradd -ms /bin/bash mpec02
RUN useradd -ms /bin/bash mpec03
RUN useradd -ms /bin/bash mpec04
RUN useradd -ms /bin/bash mpec05
RUN useradd -ms /bin/bash mpec06
RUN useradd -ms /bin/bash mpec07
RUN useradd -ms /bin/bash mpec08
RUN useradd -ms /bin/bash mpec09
RUN useradd -ms /bin/bash mpec10

RUN useradd -ms /bin/bash proj01
RUN useradd -ms /bin/bash proj02
RUN useradd -ms /bin/bash proj03
RUN useradd -ms /bin/bash proj04
RUN useradd -ms /bin/bash proj05
RUN useradd -ms /bin/bash proj06
RUN useradd -ms /bin/bash proj07
RUN useradd -ms /bin/bash proj08
RUN useradd -ms /bin/bash proj09
RUN useradd -ms /bin/bash proj10

RUN echo 'mpec01:mpec01-123' |chpasswd
RUN echo 'mpec02:mpec02-123' |chpasswd
RUN echo 'mpec03:mpec03-123' |chpasswd
RUN echo 'mpec04:mpec04-123' |chpasswd
RUN echo 'mpec05:mpec05-123' |chpasswd
RUN echo 'mpec06:mpec06-123' |chpasswd
RUN echo 'mpec07:mpec07-123' |chpasswd
RUN echo 'mpec08:mpec08-123' |chpasswd
RUN echo 'mpec09:mpec09-123' |chpasswd
RUN echo 'mpec10:mpec10-123' |chpasswd

RUN echo 'proj01:proj01-xyz' |chpasswd
RUN echo 'proj02:proj02-xyz' |chpasswd
RUN echo 'proj03:proj03-xyz' |chpasswd
RUN echo 'proj04:proj04-xyz' |chpasswd
RUN echo 'proj05:proj05-xyz' |chpasswd
RUN echo 'proj06:proj06-xyz' |chpasswd
RUN echo 'proj07:proj07-xyz' |chpasswd
RUN echo 'proj08:proj08-xyz' |chpasswd
RUN echo 'proj09:proj09-xyz' |chpasswd
RUN echo 'proj10:proj10-xyz' |chpasswd

RUN useradd -ms /bin/bash martin
RUN useradd -ms /bin/bash paul
RUN useradd -ms /bin/bash dave

RUN echo 'martin:gallagher$123' |chpasswd
RUN echo 'paul:connolly$123' |chpasswd
RUN echo 'dave:topping$123' |chpasswd



RUN service ssh start
ENTRYPOINT service ssh restart && bash



#RUN make NETCDFLIB=-L/usr/lib/x86_64-linux-gnu/ NETCDFMOD=/usr/include/ FFLAGS='-O2 -w -o' FFLAGS2='-O2 -w -o' FFLAGSOMP='-O2 -w -o'

# app is installed

