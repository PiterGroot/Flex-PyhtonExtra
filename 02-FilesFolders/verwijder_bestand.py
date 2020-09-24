#import os api
import os

bestand = input("Welk bestand wil je verwijderen? >>> ")
if(len(bestand) > 0):
    if(os.path.exists(bestand)):
        os.remove(bestand)
        print("Het bestand " + " is verwijderd, jammer dan.")
    else:
        print("Dit bestand bestaat niet, sorry")
else:
    print("Geen invoer, script zal stoppen")
