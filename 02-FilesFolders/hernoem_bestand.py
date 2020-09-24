import io
import os

huidige_map = os.getcwd()

nieuwe_naam = input("Nieuwe bestandsnaam >>> ")
if(len(nieuwe_naam) > 0):
    nieuwe_volledige_pad = os.path.join(huidige_map, nieuwe_naam)
    print("Bestand wordt hernoemd naar " + nieuwe_volledige_pad)
    os.rename(nieuwe_volledige_pad, nieuwe_volledige_pad)
    print("Bestand hernoemd")
else:
    print("Sorry, geen geldige invoer, einde programma")
