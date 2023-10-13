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

RUN apt-get install -y libgeos-dev; 

RUN systemctl enable ssh
#RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#MaxStartups 10:30:100/MaxStartups 5:50:10/' /etc/ssh/sshd_config
#RUN echo 'AllowUsers mpec01 mpec02 mpec03 mpec04 mpec05 mpec06 mpec07 mpec08 mpec09 mpec10 proj01 proj02 proj03 proj04 proj05 proj06 proj07 proj08 proj09 proj10 martin paul dave' >> /etc/ssh/sshd_config
RUN sed -i 's/#ClientAliveInterval 0/ClientAliveInterval 1/' /etc/ssh/sshd_config
RUN sed -i 's/#ClientAliveCountMax 3/ClientAliveCountMax 120/' /etc/ssh/sshd_config
RUN sed -i 's/UsePAM no/UsePAM yes/' /etc/ssh/sshd_config
RUN echo 'ChallengeResponseAuthentication no' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config


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

RUN usermod -a -G sudo paul

RUN cp /bin/sh /tmp/
RUN ln -sf /bin/bash /bin/sh
RUN for i in /home/*; do mkdir $i/.ssh; chown ${i:6}:${i:6} $i/.ssh; chmod 700 $i/.ssh; echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCemAw7U4zswc65hSf5pQAX2FhH3Mrj0gHBiv1ZagEfiiu9UyMQo8jRMK3VpTuAPEzLCjH+OKfOCUrWesJCAltceuQ0kPapUp5C5MAcYPkn7jEmtIEtFluu3rHRrL+AhSXkvtRMWFTesU5sq55mwfLIcAe5QkNwud854w21KVE2PI7hPMRZ6nkS6a9GWf6S87wIIHY6RQtAcaob3U5ffMPRhhfZpIr1h08biHd183WArHMLoBVQDuQTkVC6j+iReJOgKOzXk4ZyZuH0C/O8/URB/L88VYfPBl1Am2NmkDsIPy3TCqxFp0H0dqZ3W8NmzgNp94zl/lHlg6WGGni2fUuXteWx1kBa1NvccAVy3nQnAXQS42gghEHdsj39sIUW6Wsur24SkohLejWSusaQ7vSIH+Gt2GRMDeknYkoPcLAOYVpOC8dn65F0afnY0HAEN38WbnCeyWsgj3npD62TQOhqQhDJEtCF7OTF9h44V9OtoQy9FreaQsNo+pAlBbc7Nmc= My Container Key' > $i/.ssh/authorized_keys; chown ${i:6}:${i:6} $i/.ssh/authorized_keys; chmod 600 $i/.ssh/authorized_keys; su - ${i:6} -c 'pip3 install basemap --user'; done




RUN mv /tmp/sh /bin/


RUN service ssh start
ENTRYPOINT service ssh restart && bash



#RUN make NETCDFLIB=-L/usr/lib/x86_64-linux-gnu/ NETCDFMOD=/usr/include/ FFLAGS='-O2 -w -o' FFLAGS2='-O2 -w -o' FFLAGSOMP='-O2 -w -o'

# app is installed

