import numpy as np
from scipy.interpolate import interp1d 


print('Printing model profile')
ind1,=np.where( np.isnan(data1['MIXR'])==False)
len1=len(ind1)
p_surf = data1['PRESS'][ind1[0]]*100. # pascal
t_surf = data1['TEMP'][ind1[0]]+273.15 # temp in K

# interpolate zcb from plcl
zinterp = interp1d(data1['PRESS'][ind1],data1['HGT'][ind1])
zinit = zinterp(data1['Pres [hPa] of the Lifted Condensation Level'])
tinit = data1['Temp [K] of the Lifted Condensation Level']
pinit = data1['Pres [hPa] of the Lifted Condensation Level']*100.0

print('zinit=' +str(zinit) + ',')
print('tinit=' +str(tinit) + ',')
print('pinit=' +str(pinit) + ',')
print('psurf=' + str(p_surf) + ',')
print('tsurf=' + str(t_surf) + ',')
print('n_levels_s=' + str(len1) + ',')
str1='q_read(1,1:' + str(len1) + ') = '
for i in range(len1):
	str1 = str1 + str(data1['MIXR'][ind1[i]]/1000.) + ', '
str1=str1 + '\n theta_read(1:' + str(len1) + ') = '
for i in range(len1):
	str1 = str1 + str(data1['THTA'][ind1[i]]) + ', '
str1=str1 + '\n rh_read(1:' + str(len1) + ') = '
for i in range(len1):
	str1 = str1 + str(data1['RELH'][ind1[i]]/100.) + ', '
str1=str1 + '\n z_read(1:' + str(len1) + ') = '
for i in range(len1):
	str1 = str1 + str(data1['HGT'][ind1[i]]) + ', '
	
print(str1)

