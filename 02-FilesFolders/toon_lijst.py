#import os api
import os

huidige_map = os.getcwd()
alle_bestanden = os.scandir(huidige_map)
print("Inhoudsopgave van de map " + huidige_map)
for bestand in alle_bestanden:
    if(bestand.is_file()):
        print(bestand.name + "(Bestand)")
    elif(bestand.is_dir()):
        print(bestand.name + "(Map)")
    else:
        print(bestand.name + "(Onbekend type")
