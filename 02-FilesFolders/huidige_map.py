#import os api
import os

werkmap = os.getcwd()
print("De huidige map is " + werkmap)

lengte_mapnaam = 0
mapnaam = ""
while lengte_mapnaam == 0:
    mapnaam = input("Welke naam wil je voor de map >>> ")
    lengte_mapnaam = len(mapnaam)
    if(lengte_mapnaam > 0):
        os.mkdir(mapnaam)
    else:
        print("Je hebt geen geldige naam ingevoerd")
print("De map " + mapnaam + " is gemaakt")
