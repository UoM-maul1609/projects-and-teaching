#! /bin/bash

sudo apt-get update
sudo apt-get install -y ipython3 shotwell x11-apps gfortran \
    libnetcdff-dev mpich make python3-netcdf4 gedit python3-matplotlib \
    vim nano python3-tqdm texlive dvipng texlive-latex-extra texlive-base texlive \
    cm-super imagemagick tkdiff python3-pip ffmpeg htop python3-pandas libgeos-dev \
    fail2ban finger

sudo apt upgrade -y

pip3 install basemap --user

sudo echo '[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
findtime = 5m
bantime = 60m
ignoreip = 127.0.0.1' > jail.local
sudo mv jail.local /etc/fail2ban/
sudo systemctl enable fail2ban
sudo systemctl start fail2ban

for i in /home/proj*; do sudo deluser ${i:6} google-sudoers; done
for i in /home/mpec*; do sudo deluser ${i:6} google-sudoers; done