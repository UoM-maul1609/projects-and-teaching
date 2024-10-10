import bs4
import urllib.request

import numpy as np
import datetime
import ssl
import os
from pathlib import Path

if __name__=="__main__":
	# path
	dataPath=pathlib.Path.home() + "/SondeData/"
	Path(dataPath).mkdir(parents=True, exist_ok=True)

	# today
	dt2=datetime.datetime.now()
	# a year ago
	dt1=dt2-datetime.timedelta(days=366)
	# number of days
	days=(dt2-dt1).days
	
	"""
		has 0 and 12Z for each sonde
	"""
	context = ssl._create_unverified_context()
	hours=['00','12']
	for i in range(days):
		for j in range(2):
			worked=False
			while worked==False:
				try:
					webstring='https://weather.uwyo.edu/cgi-bin/sounding?region=' + \
						'mideast&TYPE=TEXT%3ALIST&YEAR=2024&MONTH=' + \
						'09&FROM=0912&TO=0912&STNM=40417'
					thisDate=(dt1+datetime.timedelta(days=i))
					thisDay=thisDate.day
					thisMonth=thisDate.month
					thisYear=thisDate.year
					
					thisDayStr=str(thisDay).zfill(2)
					thisMonthStr=str(thisMonth).zfill(2)
					thisYearStr=str(thisYear)
					
					newWebstring=webstring.replace('YEAR=2024','YEAR=' + thisYearStr)
					newWebstring=newWebstring.replace('MONTH=09','MONTH=' + thisMonthStr)
					newWebstring=newWebstring.replace('0912',thisDayStr + hours[j])
					
					print(newWebstring)
					
					# https://stackoverflow.com/questions/30951657/download-only-the-text-from-a-webpage-content-in-python
					
					wp=urllib.request.urlopen(newWebstring,context=context)
					soup = bs4.BeautifulSoup(wp)
					
					#print(soup.get_text())
					
					# now, save this to a file in home folder
					info=newWebstring.split('=')
					fp = open(dataPath + '/loc_' + info[-1] + '_' + \
						thisYearStr + '-' + thisMonthStr + '-' + \
						thisDayStr + '_' + hours[j] + '.txt','w')
					
					fp.write(soup.get_text())
					worked=True
				except:
					print('Failed. Trying again.')
					pass
						
					
					fp.close()