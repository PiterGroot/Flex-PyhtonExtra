import re
import os

emails = []

with open("tekstmetemails.txt", "r") as bestand:

    regel = bestand.readline()

    while regel:

        # Vul de juiste regular expression voor een email in op de puntjes
        patroon = r"[^@]+@[^@]+\.[^@]+"

        # Gebruik de juiste code op de plaats van de puntjes
        gevonden = re.findall(patroon, regel)

        # Alle gevonden emails aan de email list toevoegen
        emails.extend(regel)

        # Volgende regel lezen
        regel = bestand.readline()

print(emails)

dontClose = input()
