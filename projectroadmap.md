#  projectroadmap.md title
## 11.03.2021 - Code Notes

Imported api from ISS website as a new variable for shortcut
ISS wesbite: http://open-notify.org/Open-Notify-API/ISS-Location-Now/

import was successful using json file

Added print(obj) statement to see full object

Noted Challenges: Package for urllib2 needed import as urllib through request call from original library
"Data" unknown based on terminal output. Variable could not be located through sample code. 

# Import databases from website: Imported libraries and databases
https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db

# Import new libraries for geospatial tracking and table creation using lat and lon
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

#Error Correction: 
##11.13.2021
Realized I didn't need the dataframe in order to create the image of the map.

#Notes for commits: 
##11.14.2021
    Git add (file name)
    Git commit -m "Note"
    Git push origin main

#Code update: 11.19.2021
## BBox
Inserted code related to a barrier box (Bbox) that could be executed within the code for a lat and lon coordinate feature. It took some time but I added a 0.01 to each boundary in order to map ourside regular lat and lon coordinates. This helped create the boundary. I have the points but for some reason the map isn't importing.


#Code update: 12.9.2021
## Adding final code
Inserted new file called workstation where I've been exprimenting with code. This is my final code submission. 
Updated final code with comments and new future areas to enhance this project.
