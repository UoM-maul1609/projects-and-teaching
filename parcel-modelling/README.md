# Parcel Modelling of Secondary Ice Production

The code repository for the Bin Microphysics Model is available at [https://github.com/UoM-maul1609/bin-microphysics-model](https://github.com/UoM-maul1609/bin-microphysics-model). This model is written in Fortran and has some associated Python scripts for analysis and plotting.

## Logging in to the virtual machine
Prof. Paul Connolly will start up the VM, give you your username, SSH key (which is a file) and the IP address of the server (VM). To login you need to open `CMD` (on windows), `terminal` if on a mac or Chromebook. You would then type:
   
    ssh -i id_virtual_students.key -X <username>@<IP-address>  

The first time you log in you may need to answer 'yes' to a question about connecting. 


## Downloading the Bin Microphysics Model

Once logged in you will be interacting the VM in the same way as you would a linux server through the terminal. To download the bin microphysics model type:
	
	git clone https://github.com/UoM-maul1609/bin-microphysics-model
	
This should download the code to the folder `bin-microphysics-model`

## Compiling the Bin Microphysics Model

You need to be in the `bin-microphysics-model` folder to compile the code. Type

	cd bin-microphysics-model
	
in the terminal / cmd window to enter the folder.

We need to then tell the computer to build the machine code executable that the computer CPU understands. This can be done by typing:

	make NETCDFLIB=-L/usr/lib/x86_64-linux-gnu/ NETCDFMOD=/usr/include/ FFLAGS='-O2 -w -o' FFLAGS2='-O2 -w -o' FFLAGSOMP='-O2 -w -o'

The `make` command tells the computer to use a file called `Makefile` which is in the `bin-microphysics-model` folder you downloaded. In this file are rules for compiling the code. There are some additional variables that we pass into the Makefile. These are `NETCDFLIB`, `NETCDFMOD`, `FFLAGS`, `FFLAGS2` and `FFLAGSOMP`, which overrides the values they are set to in the Makefile. They need to be altered for our environment. 

## Running the Bin Microphysics Model

You can run the model after it has been compiled by typing

	./run.sh python/namelist-sip.in

Note that `python/namelist-sip.in` is the input file for the model, and includes initial values and processes that the model will consider. 

This generates a file called `/tmp/<username>/output1.nc`, which is a so-called NetCDF formatted file containing the model output data. 

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

## How to change the factors you are investigating

These are defined in the `runsDefine.py` file. This file has a list called `runToDo`. Each element in the list is also a list of length 2. The first element (in each length-2 list) is the default case (in the base input file, `python/namelist-sip.in`) and the second element is the comparison that you are making for that factor. 

Note, if you would like to look into different aerosol distributions you may wish to use [James et al (2023)](https://acp.copernicus.org/articles/23/9099/2023/acp-23-9099-2023.html). They reference a paper by Crooks *et al.* (2018) in their Table 3. This paper also uses the same model suggested in this project.

The mode-2 process was investigated at the University of Manchester and a paper was written about it [(James *et al.*, 2021)](https://acp.copernicus.org/articles/21/18519/2021/). 

Note, a pre-print of a paper about a recent project is in the Earth System Science Data journal, [Finney *et al. (2023)](https://essd.copernicus.org/preprints/essd-2023-303/essd-2023-303.pdf).

## References

1. Teller and Levin, Factorial method as a tool for estimating the relative contribution to precipitation of cloud microphysical processes and environmental conditions: Method and application, 2008, https://doi.org/10.1029/2007JD008960
2. James, R. L., Phillips, V. T. J., and Connolly, P. J.: Secondary ice production during the break-up of freezing water drops on impact with ice particles, Atmos. Chem. Phys., 21, 18519–18530, https://doi.org/10.5194/acp-21-18519-2021, 2021.
3. James, R. L., Crosier, J., and Connolly, P. J.: A bin microphysics parcel model investigation of secondary ice formation in an idealised shallow convective cloud, Atmos. Chem. Phys., 23, 9099–9121, https://doi.org/10.5194/acp-23-9099-2023, 2023
4. Finney, D. L., Blyth, A. M., Gallagher, M., Wu, H., Nott, G., Biggerstaff, M., Sonnenfeld, R. G., Daily, M., Walker, D., Dufton, D., Bower, K., Boeing, S., Choularton, T., Crosier, J., Groves, J., Field, P. R., Coe, H., Murray, B. J., Lloyd, G., Marsden, N. A., Flynn, M., Hu, K., Thamban, N. M., Williams, P. I., McQuaid, J. B., Robinson, J., Carrie, G., Moore, R., Aulich, G., Burton, R. R., and Connolly, P. J.: DCMEX coordinated aircraft and ground observations: Microphysics, aerosol and dynamics during cumulonimbus development, Earth Syst. Sci. Data Discuss. [preprint], https://doi.org/10.5194/essd-2023-303, in review, 2023