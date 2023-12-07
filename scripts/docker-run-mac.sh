#! /bin/bash

ssh-keygen -R [127.0.0.1]:2022
xhost +local:docker
docker run  -it --rm -e DISPLAY=host.docker.internal:0 -p 2022:22 -v /tmp/.x11-unix:/tmp/.x11-unix ghcr.io/uom-maul1609/projects-and-teaching
