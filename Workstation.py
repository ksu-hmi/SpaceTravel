#imports for this project
import urllib.request as urllib2
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geoplotlib

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read())

# print(obj['timestamp'])
# print(obj['iss_position']['latitude'], obj['data']['iss_position']['latitude'])

lat = float(obj['iss_position']['latitude'])
lon = float(obj['iss_position']['longitude'])
print(lat)
print(lon)

# lat and lon variabels are string variabels coded as unicode. Need to decipher and change to float variable in order to move forward. CHALLENGE ACCEPTED
# Created data frame (df) for mapping shell, modified existing code to account for my new variables lat, lon. 
# d = {'lat': lat, 'lon': lon}
# df = pd.DataFrame(data=d)
# df.head()

# print(df)

#df example of expected output
# #    col1  col2
# # 0     1     3
# # 1     2     4

#Creating box for geosptial mapping using current ISS lat and lon variables to expand 4 corners for mapping. 
# BBox is a code used to create the actual 4 corners of the shell for the map in order to pinpoint the location of the ISS within those corners.
#offset = 10

BBox = {"lat": [lat, lat+0.01], "lon": [lon, lon+0.01]}
print(BBox)

# (46.5691,46.8398, 24.6128, 24.8256) Received expected output of lat, lon.

#imported new libraries for geoplotlib and pyglet to enable calculation of geoplots using coordinates from lat, lon using ISS api variables.

geoplotlib.dot(BBox)
#error received on code when calling BBox. Added a colon to .dot function for BBox call. :P
geoplotlib.show()
#successfully generated map shape file of the world, but can't see the plot of the ISS location. 
# Not sure if the location of the ISS needs to be maximized on the map in order to see or if it's just not plotted.
#CHALLENGE ACCEPTED

# ##NOT SURE HOW TO GET THIS CODE TO WORK OR IF NEEDED
# ruh_m = plt.imread('C:/.. … /Riyadh_map.png') 

# fig, ax = plt.subplots(figsize = (8,7))
# ax.scatter(lon, lat, zorder=1, alpha= 0.2, c='b', s=10)
# ax.set_title('Plotting Spatial Data on Riyadh Map')
# ax.set_xlim(lat,lat + 1)
# ax.set_ylim(lon,lon + 1)
# ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
