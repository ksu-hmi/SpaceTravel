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


