# Projects and Teaching
This repository describes how to set-up your system to run many of the numerical models at [https://github.com/UoM-maul1609](https://github.com/UoM-maul1609).

I have set up some Virtual Machines (VMs) for you to use and I will explain how you can use these. Why not just run the code on my own computer? There are two main reasons for the models used at [https://github.com/UoM-maul1609](https://github.com/UoM-maul1609). 

Firstly, for models that are written in Python, you would need to install Python and all the necessary libraries to be able to run the model. This can be a pain at times. Using a VM we are able to ship Python and all the necessary libraries we need to run the python code, so no installation by you is necessary.  

Secondly, for models that are written in Fortran, you would need to install a Fortran compiler, NetCDF libraries and MPI libraries and then compile the model for your system. This can also be a pain. Using a VM we can also ship all the necessary compilers, libraries and other tools to enable you to quickly and easily get up to speed. You will connect to the VM using a client computer (usually your laptop)

# Other software to install

If you are running the windows operating system you may find it useful to install [Xming](https://sourceforge.net/projects/xming/). This will enable you to open up windows thorugh the terminal when you log in to the VM. Xming needs to be started and runs in the background before you connect to the VM.

If you are using a Chromebook you should enable the linux developer tools. Search for it and enable it.

If you are using a mac, you may find it useful to install [XQuartz](https://www.xquartz.org), which is the same as Xming, but for the mac. XQuartz needs to be started and runs in the back ground before you connect to the VM.


# Example taught module
If you are using the VMs in one of my taught modules this is probably because you are working off-campus. We have servers you can connect to when on campus. While the instructions are very similar, the IP addresses and authentication will be slightly different. 

# Help with Linux commands
[Here](https://cheatography.com/davechild/cheat-sheets/linux-command-line/) is a useful cheatsheet for useful linux commands.

A more thorough description of some commands is [here](https://www.digitalocean.com/community/tutorials/linux-commands)

# Projects
Here are details of projects:
 
1. [Single Column Modelling](scm-precipitation-modelling/README.md)
2. [Secondary Ice Modelling](parcel-modelling/README.md)
3. [Saturn's Hexagon](saturn-hexagon-modelling/README.md)
4. [Marine Cloud Brightening](mcb-modelling/README.md)

