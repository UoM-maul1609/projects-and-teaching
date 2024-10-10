import matplotlib.pyplot as plt
import os
import tephi
from tephi import Tephigram
import numpy as np

ind,=np.where(np.isnan(data1['DWPT'])==False)
dewpoint = list(zip(data1['PRESS'][ind], data1['DWPT'][ind]))
ind,=np.where(np.isnan(data1['TEMP'])==False)
drybulb = list(zip(data1['PRESS'][ind], data1['TEMP'][ind]))

ind,=np.where(np.isnan(data1['SKNT'])==False)
barbs = list(zip(data1['SKNT'][ind], data1['DRCT'][ind], data1['PRESS'][ind]))

anchor = [(1000, -20), (200, -20)]
figure=plt.figure(figsize=(8,8))
tephigram = Tephigram(figure=figure, anchor=anchor)
profile = tephigram.plot(dewpoint, label='Dew Point Temperature', color='blue')
profile.barbs(barbs)
tephigram.plot(drybulb, label='Dry Bulb Temperature', color='red')


#plt.axis((1600,1800,1680,1900))  

