#! /bin/bash

ssh-keygen -R [127.0.0.1]:2022
xhost +local:docker
docker run  -it --rm -e DISPLAY=$DISPLAY --net=host -v /tmp/.x11-unix:/tmp/.x11-unix ghcr.io/uom-maul1609/projects-and-teaching-all
