import numpy as np
from scipy.interpolate import interp1d 




def do_it(data1):
    #print('Printing model profile')
    ind1,=np.where( np.isnan(data1['MIXR'])==False)
    len1=len(ind1)
    p_surf = data1['PRESS'][ind1[0]]*100. # pascal
    t_surf = data1['TEMP'][ind1[0]]+273.15 # temp in K

    # interpolate zcb from plcl
    zinterp = interp1d(data1['PRESS'][ind1],data1['HGT'][ind1])
    zinit = zinterp(data1['Pres [hPa] of the Lifted Condensation Level'])
    tinit = data1['Temp [K] of the Lifted Condensation Level']
    pinit = data1['Pres [hPa] of the Lifted Condensation Level']*100.0

    #print('zinit=' +str(zinit) + ',')
    #print('tinit=' +str(tinit) + ',')
    #print('pinit=' +str(pinit) + ',')
    #print('psurf=' + str(p_surf) + ',')
    #print('tsurf=' + str(t_surf) + ',')
    #print('n_levels_s=' + str(len1) + ',')
    q_read='q_read(1,1:' + str(len1) + ') = '
    for i in range(len1):
        q_read = q_read + str(data1['MIXR'][ind1[i]]/1000.) + ', '
    theta_read='theta_read(1:' + str(len1) + ') = '
    for i in range(len1):
        theta_read = theta_read + str(data1['THTA'][ind1[i]]) + ', '
    rh_read='rh_read(1:' + str(len1) + ') = '
    for i in range(len1):
        rh_read = rh_read + str(data1['RELH'][ind1[i]]/100.) + ', '
    z_read='z_read(1:' + str(len1) + ') = '
    for i in range(len1):
        z_read = z_read + str(data1['HGT'][ind1[i]]) + ', '

    z_read = z_read[:-2] + '/ \n'
    str1=q_read + '\n ' + theta_read + '\n ' + rh_read + '\n ' + z_read
    #print(str1)


    z_replace='zinit=' +str(zinit) + ','
    t_replace='tinit=' +str(tinit) + ','
    p_replace='pinit=' +str(pinit) + ','
    ps_replace='psurf=' + str(p_surf) + ','
    ts_replace='tsurf=' + str(t_surf) + ','
    n_level_replace='n_levels_s=' + str(len1) + ','

    return (q_read,theta_read,rh_read,z_read,z_replace,t_replace,p_replace,ps_replace,ts_replace,n_level_replace)

if __name__=="__main__":
    (q_read,theta_read,rh_read,z_read,z_replace,t_replace,\
            p_replace,ps_replace,ts_replace,n_level_replace)=do_it(data1)
