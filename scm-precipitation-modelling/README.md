# Single Column Modelling

The code repository for the Single Column Model is available at [https://github.com/UoM-maul1609/simple-cloud-model](https://github.com/UoM-maul1609/simple-cloud-model). This model is written in Fortran and has some associated Python scripts for analysis and plotting.

## Logging in to the container instance
Prof. Paul Connolly will start up the container instance, give you your username, key and the IP address of the server. To login you need to open `CMD` (on windows), `terminal` if on a mac or Chromebook. You would then type:
   
    ssh -i id_container.key -X <username>@<IP-address>  

The first time you log in you may need to answer 'yes' to a question about connecting. 


## Downloading the Single Column Model

Once logged in you will be interacting the container instance in the same way as linux server through the terminal. To download the single column model type:
	
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

	./main.exe namelist.pamm

Note that `namelist.pamm` is the input file for the model, and includes initial values and processes that the model will consider. 

This generates a file called `/tmp/output.nc`, which is a so-called NetCDF formatted file. 

## Plotting the output

We can use Python to look at the output. There is an example script at `python/scm_plot.py`. This can be edited to output different variables from the NetCDF file. To plot the output file at `/tmp/output.nc` you can type:

	python3 python/scm_plot.py
	
This will generate a file at `/tmp/scm_plot.png`

## Obtaining the output file
How to we obtain the output file from inside the container, so that we can view it or insert it in a report?

We can open up another `CMD`, or `terminal` window  and connect with SFTP (Secure File Transfer Protocol). 

From another terminal or CMD window type

	sftp -i id_container.key <username>@<IP-address>
	
This will log you into the container instance. You can bring the file over to your local system by typing

	get /tmp/scm_plot.png
	
And then you will be able to view it in the usual way. By default it will be transferred to the folder that you were in before you logged in with ssh. 

## Factorial Analysis

A neat way of understanding how different factors impact precipitation on the ground is the Factorial Method. See [https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007JD008960](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007JD008960)

This has been coded up for you for certain factors, but we will discuss factors for you to look at in your project. 

To run the factorial analysis code you can run the model using the `batchRuns.py` script. There are 6 factors by default and each factor has two choices, so this is 2^6^ =64 simulations. 64 output files will be put in `/tmp/`. To run it type:
	
	cd python
	python3 batchRuns.py

In order to analyse these results we can use the `factorialMethod.py` script. Type:

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

Whereas the interactions are the 'non-linear' interactions between factors. For example making the cloud 'deeper' (the first factor) gives more rain. Turning off the warm-rain process (4th factor) gives less rain. But making the cloud deeper AND turning off the warm rain process has a negative interaction (first row and 4th column in the table). This means that you get more rain from a deeper cloud and switching warm rain on than their combined linear effects. 
## References

1. Teller and Levin, Factorial method as a tool for estimating the relative contribution to precipitation of cloud microphysical processes and environmental conditions: Method and application, 2008, https://doi.org/10.1029/2007JD008960