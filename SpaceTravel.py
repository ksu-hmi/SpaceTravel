#imports for this project
import urllib.request as urllib2
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geoplotlib

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read()


# print(obj['timestamp'])
# print(obj['iss_position']['latitude'], obj['data']['iss_position']['latitude'])

lat = float(obj['iss_position']['latitude'])
lon = float(obj['iss_position']['longitude'])
print(lat)
print(lon)

#lat and lon variabels are string variabels coded as unicode. Need to decipher and change to float variable in order to move forward. CHALLENGE ACCEPTED
#Created data frame (df) for mapping shell, modified existing code to account for my new variables lat, lon. 
# d = {'lat': lat, 'lon': lon}
# df = pd.DataFrame(data=d)
# df.head()

# print(df)

#df example of expected output
# #    col1  col2
# # 0     1     3
# # 1     2     4

## Realized I didn't need the dataframe in order to create the image of the map.

#Creating box for geosptial mapping using current ISS lat and lon variables to expand 4 corners for mapping. 
# BBox is a code used to create the actual 4 corners of the shell for the map in order to pinpoint the location of the ISS within those corners.
#offset = 10

BBox = {"lat": [lat, lat+0.01], "lon": [lon, lon+0.01]}
print(BBox)