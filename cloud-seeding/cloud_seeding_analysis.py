import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import getpass

username=getpass.getuser()
num_runs=96
precip1=np.zeros(num_runs)
precip2=np.zeros(num_runs)

for i in range(num_runs):
    n=str(i)
    nc=Dataset('/tmp/' + username + '/output' + n.zfill(3) + '.nc')
    precip = nc['precip'][:]
    precip1[i] = np.sum(precip*10./3600.)
    nc.close()

for i in range(8):
    n=str(i)
    nc=Dataset('/tmp/' + username + '/outputseed' + n.zfill(3) + '.nc')
    precip = nc['precip'][:]
    precip2[i] = np.sum(precip*10./3600.)
    nc.close()


plt.ion()
plt.plot(precip1,'.')
plt.plot(precip2,'.')
