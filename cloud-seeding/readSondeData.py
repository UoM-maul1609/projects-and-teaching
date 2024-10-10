import numpy as np
import datetime
import os
from pathlib import Path
import glob 
from scipy.interpolate import interp1d  

def interpolateData(dats,whichOne):
	num=len(dats)
	height_array=np.mgrid[0:30000:200]
	num_z=len(height_array)
	arr=np.zeros((num_z,num))
	for i in range(num):
		myinterp=interp1d(dats[i]['HGT'],dats[i][whichOne],bounds_error=False)
		arr[:,i]=myinterp(height_array)
	return (arr,height_array)

def readOneFile(fileName):
	fp = open(fileName,'r')
	data=fp.readlines()
	fp.close()
	str1='-----------------------------' +\
	'------------------------------------------------'
	str2='Station information and sounding indices'
	ind1 = [indx for indx in range(len(data)) if str1 in data[indx]]
	ind2 = [indx for indx in range(len(data)) if str2 in data[indx]]

	if len(ind1)==0:
		return dict()
	
	data1=dict()
	num1=ind2[0]-ind1[1]-1
	press=np.zeros(num1)
	hgt=np.zeros(num1)
	temp=np.zeros(num1)
	dwpt=np.zeros(num1)
	relh=np.zeros(num1)
	mixr=np.zeros(num1)
	drct=np.zeros(num1)
	sknt=np.zeros(num1)
	thta=np.zeros(num1)
	thte=np.zeros(num1)
	thtv=np.zeros(num1)
	for i in range(ind1[1]+1,ind2[0]):
		line1=data[i]  
		press[i-ind1[1]-1]=np.nan if ( line1[0:7].isspace()) else float(line1[0:7])
		hgt[i-ind1[1]-1]=np.nan if ( line1[7:14].isspace()) else float(line1[7:14])
		temp[i-ind1[1]-1]=np.nan if ( line1[14:21].isspace()) else float(line1[14:21])
		dwpt[i-ind1[1]-1]=np.nan if ( line1[21:28].isspace()) else float(line1[21:28])
		relh[i-ind1[1]-1]=np.nan if ( line1[28:35].isspace()) else float(line1[28:35])
		mixr[i-ind1[1]-1]=np.nan if ( line1[35:42].isspace()) else float(line1[35:42])
		drct[i-ind1[1]-1]=np.nan if ( line1[42:49].isspace()) else float(line1[42:49])
		sknt[i-ind1[1]-1]=np.nan if ( line1[49:56].isspace()) else float(line1[49:56])
		thta[i-ind1[1]-1]=np.nan if ( line1[56:63].isspace()) else float(line1[56:63])
		thte[i-ind1[1]-1]=np.nan if ( line1[63:70].isspace()) else float(line1[63:70])
		thtv[i-ind1[1]-1]=np.nan if ( line1[70:77].isspace()) else float(line1[70:77])
	
	data1['PRESS']=press
	data1['HGT']=hgt
	data1['TEMP']=temp
	data1['DWPT']=dwpt
	data1['RELH']=relh
	data1['MIXR']=mixr
	data1['DRCT']=drct
	data1['SKNT']=sknt
	data1['THTA']=thta
	data1['THTE']=thte
	data1['THTV']=thtv
	
	
	str1=['Station latitude','Station longitude','Station elevation', \
		'Showalter index', 'Lifted index', \
		'LIFT computed using virtual temperature', \
		'SWEAT index', 'K index','Cross totals index', \
		'Vertical totals index', 'Totals totals index', \
		'Convective Available Potential Energy', \
		'CAPE using virtual temperature', \
		'Convective Inhibition', \
		'CINS using virtual temperature', \
		'Bulk Richardson Number', \
		'Bulk Richardson Number using CAPV',\
		'Temp [K] of the Lifted Condensation Level', \
		'Pres [hPa] of the Lifted Condensation Level', \
		'Equivalent potential temp [K] of the LCL', \
		'Mean mixed layer potential temperature',\
		'Mean mixed layer mixing ratio', \
		'1000 hPa to 500 hPa thickness', \
		'Precipitable water [mm] for entire sounding']
	for i in range(len(str1)):
		ind = [indx for indx in range(len(data)) \
			if str1[i] in data[indx]]
		try:
			data1[str1[i]]=float(data[ind[0]].split(': ')[1])
		except:
			data1[str1[i]]=np.nan

	ind = [indx for indx in range(len(data)) \
		if 'Observation time' in data[indx]]
	try:
		var=data[ind[0]].split(': ')[1]
		data1['Observation time']=datetime.datetime(year=2000+int(var[:2]), \
			month=int(var[2:4]),day=int(var[4:6]),\
			hour=int(var[7:9]),minute=int(var[9:]))
	except:
		data1['Observation time']=np.nan
	return data1

if __name__=="__main__":
	# path
	dataPath=Path.home() 
	dataPath=dataPath.joinpath("SondeData/")
	d=str(dataPath.joinpath('*.txt'))
	files=glob.glob(d)
	files.sort()
		
	
		
	tlcl=np.zeros(len(files))
	plcl=np.zeros(len(files))
	pw=np.zeros(len(files))
	cape=np.zeros(len(files))
	cin=np.zeros(len(files))
	time=[]
	k=0
	dats=[]
	for i in range(len(files)):	
		print(str(i) + ' ' + files[i])
		try:
			data1=readOneFile(files[i])
			if(len(data1)):
				time.append(data1['Observation time'])
				pw[k]=data1['Precipitable water [mm] for entire sounding']
				tlcl[k]=data1['Temp [K] of the Lifted Condensation Level']
				plcl[k]=data1['Pres [hPa] of the Lifted Condensation Level']
				cape[k]=data1['Convective Available Potential Energy']
				cin[k]=data1['Convective Inhibition']
				k += 1
				dats.append(data1)
		except:
			pass	
				
	pw=pw[:k]
	tlcl=tlcl[:k]
	plcl=plcl[:k]
	cape=cape[:k]
	cin=cin[:k]
	
	
	(arr,height_array)=interpolateData(dats,'THTA')	
	(arr2,height_array)=interpolateData(dats,'MIXR')	
	(arr2,height_array)=interpolateData(dats,'RELH')
