#{ location: new google.maps.LatLng(40.416775, -3.70379), weight: 6 }

#Script to convert longitude and latitude into a friendly format for the Google Maps API
import pandas

importData = pandas.read_csv('weightedDataFrame.csv')

heatpointList = []

for elementIndex, elementValue in enumerate(importData["weight"]):

    heatpointList.append(("{ location: new google.maps.LatLng(" + str(importData["latitude"][elementIndex]) + "," + str(importData["longitude"][elementIndex]) + "), weight: " + str(importData["weight"][elementIndex]) + "},"))

with open(r'/Users/jackal/Desktop/HackathonProject/list.txt', 'w') as fp:
    for item in heatpointList:
        fp.write("%s\n" % item)
    print('Done')
