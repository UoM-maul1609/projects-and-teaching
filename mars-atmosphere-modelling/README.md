# Modelling the Evolution of the Martian Atmosphere

## What the project is about
Mars is currently a cold and dry planet. However, observations of the geology on Mars suggests that this has not always been so. There is evidence of erosion by fluvial activity, ancient lakes and widespread weathering on the its surface. This provides strong evidence that Mars was once a 'warm and wet' planet. In the 'Noachian' period, between 4 and 3.6 billion years ago, there is evidence of prolonged wet periods, which is supported by clay minerals in rocks of this age. Recent modelling suggests episodes of warm and wet conditions occurred during the 'Hesperian' period, some 3.2 to 3.6 billion years ago, which is also supported by the longevity of lakes (Mangold, 2021).  However, observations of the isotopic abundance of N14, and noble gases in the atmosphere suggest that Mars lost its atmosphere around 4 billion years ago (Kurokawa, et al. 2018). After atmospheric loss occurs it is difficult to produce conditions that are warm and wet. 
In this project you will use a model of the evolution of the Martian atmosphere. The model simulates the atmospheric pressure loss due to impact erosion, sputtering and photochemical escape in addition to replenishment due to impacts, volcanic degassing, and gas deposition. It calculates the abundance of several elements and their isotopic abundance, which can be compared with observations. Time-permitting you will investigate factors that may be able to explain the episodic warm and wet conditions that are thought to occur into the Hesperian.

## Code

The code repository for the Mars Atmospheric History Model is available at [https://github.com/maul1609/mars-atmosphere-history](https://github.com/maul1609/mars-atmosphere-history). This model is written in Python for analysis and plotting.

## Logging in to the virtual machine
Prof. Paul Connolly will start up the VM, give you your username, SSH key (which is a file) and the IP address of the server (VM). To login you need to open `CMD` (on windows), `terminal` if on a mac or Chromebook. You would then type:
   
    ssh -i id_virtual_students.key -X <username>@<IP-address>  

The first time you log in you may need to answer 'yes' to a question about connecting. 


## Downloading the Mars Atmosphere History Model

Once logged in you will be interacting the VM in the same way as you would a linux server through the terminal. To download the Mars atmosphere history model type:
	
	git clone https://github.com/maul1609/mars-atmosphere-history
	
This should download the code to the folder `mars-atmosphere-history`

	

## References

1. Kurokawa H, Kurosawa K,  Usui T, A lower limit of atmospheric pressure on early Mars inferred from nitrogen and argon isotopic compositions, Icarus, 2018, 443-459, https://doi.org/10.1016/j.icarus.2017.08.020

2. Mangold, N. Intermittent warmth on young Mars, 2021, 112-117, https://doi.org/10.1038/s41561-021-00700-9

