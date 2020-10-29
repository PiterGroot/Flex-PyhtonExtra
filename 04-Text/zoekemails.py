import re
import os

emails = []


with open("tekstmetemails.txt", "r") as bestand:

    regel = bestand.readline()

    while regel:

        # Vul de juiste regular expression voor een email in op de puntjes
        patroon = r"^\S+@\S+$"

        # Gebruik de juiste code op de plaats van de puntjes
        gevonden = re.findall(patroon, regel)

        # Alle gevonden emails aan de email list toevoegen
        emails.append(gevonden)

        # Volgende regel lezen
        regel = bestand.readline()

print(list)
dontClose = input()
