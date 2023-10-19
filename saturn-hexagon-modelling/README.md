# Saturn's Hexagon

## What the project is about

In the 80s the Voyager missions delivered images of a hexagonal structure around the north pole of Saturn. Striking optical images were later delivered by the Cassini mission in the 2010s. This structure was later revealed to be a Rossby wave in the atmosphere of Saturn. But how and why does it form? This will be the topic of this project. To answer this question you will use a shallow-water model mapped on to a sphere and perform numerical simulations of an atmospheric jet in the northern hemisphere of Saturn. You will experiment with different jet speeds, and thicknesses in addition to other variables. Depending on your interests you may also experiment with linear wave theory to understand why there are 6-sides to the Rossby wave and delve into why the Rossby wave moves as it does. 

## Code
The code repository for the Shallow Water Model on Sphere is available at [https://github.com/UoM-maul1609/shallow-water-model-on-sphere](https://github.com/UoM-maul1609/shallow-water-model-on-sphere). This model is written in Fortran and has some associated Python scripts for analysis and plotting.

## Logging in to the virtual machine
Prof. Paul Connolly will start up the VM, give you your username, SSH key (which is a file) and the IP address of the server (VM). To login you need to open `CMD` (on windows), `terminal` if on a mac or Chromebook. You would then type:
   
    ssh -i id_virtual_students.key -X <username>@<IP-address>  

The first time you log in you may need to answer 'yes' to a question about connecting. 


## Downloading the Shallow Water Model

Once logged in you will be interacting the VM in the same way as you would a linux server through the terminal. To download the shallow water model type:
	
	git clone https://github.com/UoM-maul1609/shallow-water-model-on-sphere
	
This should download the code to the folder `shallow-water-model-on-sphere`

## Compiling the Shallow Water Model

You need to be in the `shallow-water-model-on-sphere` folder to compile the code. Type

	cd shallow-water-model-on-sphere
	
in the terminal / cmd window to enter the folder.

We need to then tell the computer to build the machine code executable that the computer CPU understands. This can be done by typing:

	make NETCDFLIB=-L/usr/lib/x86_64-linux-gnu/ NETCDFMOD=/usr/include/ FFLAGS='-O2 -w -o' FFLAGS2='-O2 -w -o' FFLAGSOMP='-O2 -w -o'

The `make` command tells the computer to use a file called `Makefile` which is in the `shallow-water-model-on-sphere` folder you downloaded. In this file are rules for compiling the code. There are some additional variables that we pass into the Makefile. These are `NETCDFLIB`, `NETCDFMOD`, `FFLAGS`, `FFLAGS2` and `FFLAGSOMP`, which overrides the values they are set to in the Makefile. They need to be altered for our environment. 

## Running the Shallow Water Model

You can run the model on 4 processors after it has been compiled by typing

	./run.sh 4

Note that `namelist.in` is the input file for the model, and includes initial values and processes that the model will consider. 

This generates a file called `/tmp/<username>/output.nc`, which is a so-called NetCDF formatted file containing the model output data. 

## Plotting the output

We can use Python to look at the output. There is an example script at `python/example_plot_bmm.py`. This can be edited to output different variables from the NetCDF file. To plot the output file at `/tmp/<username>/output1.nc` you can type:

	python3 python/example_plot_bmm.py
	
This will generate a file at `/tmp/<username>/Test.png`

## Obtaining the output file
How to we obtain the output file from inside the container, so that we can view it or insert it in a report?

We can open up another `CMD`, or `terminal` window  and connect with SFTP (Secure File Transfer Protocol). 

From another terminal or CMD window type

	sftp -i id_virtual_students.key <username>@<IP-address>
	
This will log you into the VM. You can bring the file over to your local system by typing

	get /tmp/<username>/Test.png
	
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
		[[ 43738.74993496]
		 [-53935.79485368]
		 [ 53299.64164086]
		 [  -539.24981414]
		 [ 48381.34649661]
		 [ 58825.67145921]]
		Interactions
		              t           aer            hm          br            m1            m2
		0           NaN -11593.413864  52866.128636  600.707490  25598.785694  -8086.938432
		1 -11593.413864           NaN   3021.430069  906.641322  15156.672129 -42487.089173
		2  52866.128636   3021.430069           NaN  -59.654391  34162.304535 -15403.547601
		3    600.707490    906.641322    -59.654391         NaN   -570.074529   -549.083881
		4  25598.785694  15156.672129  34162.304535 -570.074529           NaN  12486.423234
		5  -8086.938432 -42487.089173 -15403.547601 -549.083881  12486.423234           NaN
	
The 'effect' is just the effect of each factor we are investigating on the maximum ice crystal number concentration in the cloud.

Whereas the interactions are the 'non-linear' interactions between factors. For example turning on the HM process (the 3rd factor) actually increases the ice in the cloud in this case. Why would that be? Turning on the Mode-2 raindrop-freezing process (6th factor) gives more ice too. These are secondary ice mechanisms, so this is expected. 

But making the turning on the HM process AND turning on the Mode-2 process has a negative interaction term (last row or the HM column in the table). This means that when both processes act together we get less ice than the sum of them individually. This is perhaps not too surprising, as there is a limit to the amount of ice we can have in the cloud.

## References

1. Ana C. Barbosa Aguiar, Peter L. Read, Robin D. Wordsworth, Tara Salter, Y. Hiro Yamazaki, A laboratory model of Saturn’s North Polar Hexagon, Icarus, Volume 206, Issue 2,
2010, Pages 755-763,
https://doi.org/10.1016/j.icarus.2009.10.022.