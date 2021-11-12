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

