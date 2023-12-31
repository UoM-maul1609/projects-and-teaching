# Single Column Modelling

## What the project is about
Understanding how clouds lead to precipitation on the ground (i.e. rainfall) is an important for weather and climate models. There are many processes that can lead to precipitation on the ground and perhaps the most uncertain are those involving the ice phase. 

Single column models are an efficient way to understand how cloud processes may affect precipitation on the ground.  In this project you will set up a single column model to simulate both a 'shallow' and a 'deep' cloud system. You will investigate how different factors affect the simulated precipitation on the ground using a statistical method known as the factorial method. Processes to investigate are how aerosols affect the initial cloud droplet and ice crystal number concentrations and also how a myriad of secondary ice mechanisms can alter precipitation patterns in both shallow and deep cloud cases. 

## Code
The code repository for the Single Column Model is available at [https://github.com/UoM-maul1609/simple-cloud-model](https://github.com/UoM-maul1609/simple-cloud-model). This model is written in Fortran and has some associated Python scripts for analysis and plotting.

## Logging in to the virtual machine
Prof. Paul Connolly will start up the VM, give you your username, SSH key (which is a file) and the IP address of the server (VM). To login you need to open `CMD` (on windows), `terminal` if on a mac or Chromebook. You would then type:
   
    ssh -i id_virtual_students.key -X <username>@<IP-address>  

The first time you log in you may need to answer 'yes' to a question about connecting. 


## Downloading the Single Column Model

Once logged in you will be interacting the VM in the same way as you would a linux server through the terminal. To download the single column model type:
	
	git clone https://github.com/UoM-maul1609/simple-cloud-model
	
This should download the code to the folder `simple-cloud-model`

## Compiling the Single Column Model

You need to be in the `simple-cloud-model` folder to compile the code. Type

	cd simple-cloud-model
	
in the terminal / cmd window to enter the folder.

We need to then tell the computer to build the machine code executable that the computer CPU understands. This can be done by typing:

	make NETCDFLIB=-L/usr/lib/x86_64-linux-gnu/ NETCDFMOD=/usr/include/ FFLAGS='-O2 -w -o' FFLAGS2='-O2 -w -o' FFLAGSOMP='-O2 -w -o'

The `make` command tells the computer to use a file called `Makefile` which is in the `simple-cloud-model` folder you downloaded. In this file are rules for compiling the code. There are some additional variables that we pass into the Makefile. These are `NETCDFLIB`, `NETCDFMOD`, `FFLAGS`, `FFLAGS2` and `FFLAGSOMP`, which overrides the values they are set to in the Makefile. They need to be altered for our environment. 

## Running the Single Column Model

You can run the model after it has been compiled by typing

	./run.sh namelist.pamm

Note that `namelist.pamm` is the input file for the model, and includes initial values and processes that the model will consider. 

This generates a file called `/tmp/<username>/output.nc`, which is a so-called NetCDF formatted file containing the model output data. 

## Plotting the output

We can use Python to look at the output. There is an example script at `python/scm_plot.py`. This can be edited to output different variables from the NetCDF file. To plot the output file at `/tmp/<username>/output.nc` you can type:

	python3 python/scm_plot.py
	
This will generate a file at `/tmp/<username>/scm_plot.png`

## Obtaining the output file
How to we obtain the output file from inside the container, so that we can view it or insert it in a report?

We can open up another `CMD`, or `terminal` window  and connect with SFTP (Secure File Transfer Protocol). 

From another terminal or CMD window type

	sftp -i id_virtual_students.key <username>@<IP-address>
	
This will log you into the VM. You can bring the file over to your local system by typing

	get /tmp/<username>/scm_plot.png
	
And then you will be able to view it in the usual way. By default it will be transferred to the folder that you were in before you logged in with SSH. 

## Factorial Analysis

A neat way of understanding how different factors impact precipitation on the ground is the Factorial Method. See [https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007JD008960](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007JD008960)

This has been coded up for you for certain factors, but we will discuss factors for you to look at in your project. 

To run the factorial analysis code you can run the model using the `batchRuns.py` script, which is in the `python` folder inside the repository. There are 6 factors by default and each factor has two choices, so this is $`2^6 =64`$ simulations. 64 output files will be put in `/tmp/<username>`. To go into the python folder enter:
	
	cd python

Then to run the code to batch process these factors type:

	python3 batchRuns.py

In order to analyse these results we can use the `factorialMethod.py` script. From inside the `python` directory, enter this command:

	python3 factorialMethod.py
	
The effect of each factor will be printed to the screen as

	Effect of x,y,z
	[[ 3.13580385e+00]
 	[-9.80905201e-07]
 	[ 8.72890989e-03]
 	[-3.11456348e+00]
 	[ 4.79087489e-03]
 	[ 2.70197272e+00]]
	Interactions
	              t           aer            hm            wr            rm           ice
	0           NaN  9.407529e-07  1.010883e-02 -3.095892e+00  1.412962e-02  3.042674e+00
	1  9.407529e-07           NaN  3.076647e-07  3.045719e-07  2.270008e-07  9.809052e-07
	2  1.010883e-02  3.076647e-07           NaN  7.741930e-03 -8.728910e-03 -8.728910e-03
	3 -3.095892e+00  3.045719e-07  7.741930e-03           NaN  7.790749e-03 -3.064033e+00
	4  1.412962e-02  2.270008e-07 -8.728910e-03  7.790749e-03           NaN -4.790875e-03
	5  3.042674e+00  9.809052e-07 -8.728910e-03 -3.064033e+00 -4.790875e-03           NaN 	
The 'effect' is just the effect of each factor we are investigating on precipitation on the ground.

Whereas the interactions are the 'non-linear' interactions between factors. For example making the cloud 'deeper' (the first factor) gives more rain (the effect is positive). Turning off the warm-rain process (4th factor) gives less rain (the effect is negative). Perhaps not too surprising. 

But making the cloud deeper AND turning off the warm rain process has a negative interaction (first row and 4th column in the table). This means that you get more rain on the ground from a deeper cloud and switching warm rain on than their combined linear effects. 

## How to change the factors you are investigating

These are defined in the `runsDefine.py` file. This file has a list called `runToDo`. Each element in the list is also a list of length 2. The first element (in each length-2 list) is the default case (in the base input file, `namelist.pamm`) and the second element is the comparison that you are making for that factor. 

## References

1. Teller and Levin, Factorial method as a tool for estimating the relative contribution to precipitation of cloud microphysical processes and environmental conditions: Method and application, 2008, https://doi.org/10.1029/2007JD008960
2. Shipway, B.J., Hill, A.A., 2012. Diagnosis of systematic differences between multiple parametrizations of warm rain microphysics using a kinematic framework. Q. J. R. Meteorol. Soc. 138, 2196–2211. https://doi.org/10.1002/qj.1913