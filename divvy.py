#This program uses the Divvy API to return the closest station and number of available
#bikes from the Young building

import json
from urllib.request import urlopen

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']
# print(stations)

def distanceToYoung(x,y):
	youngX = 41.793414
	youngY = -87.600915
	return (((x-youngX)**2)+((y-youngY)**2))**.5

closestDistance = 99999999
closestLocation = ""
closestBikes = 0

for station in stations:
	lat = station['latitude']
	lon = station['longitude']
	distance = distanceToYoung(lat,lon)
	if distance < closestDistance :
		closestDistance = distance
		closestLocation = station['stAddress1']
		closestBikes = station['availableBikes']

print ("The closest Divvy station to the Young building is ",closestLocation)
print ("There are currently ",closestBikes," bikes available there")

#here there should be an if statement here that returns the next closest station 
#if the number of available bikes is zero
# if closestBikes == 0: ...






# The Young building has the following latitude and longitude: 41.793414,-87.600915.
# To measure surface distance, you can treat latitudes and longitudes like x and y coordinates, and calculate distance between locations with the usual Euclidean distance formula.

# 1. Modify the code above to display the station name and number of available bikes for the station closest to Young.

# You will likely want to consult the JSON stream from Divvy

# - http://www.divvybikes.com/stations/json
