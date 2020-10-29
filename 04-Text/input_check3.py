import re



while True:
    nummer = input("Voer je mobiele nummer in >>>> ")
    code = input("Voer je postcode in >>>> ")
    kenteken = input("Voer je kenteken in >>>> ")
    patroon = "^06-?\d{8}"
    patroon1 = "^\d{4}\s?[a-zA-Z]{2}"
    patroon2 = "^\d{2}-?[A-Z]{3}-?\d{3}"
    matches = re.findall(patroon, nummer)
    matches1 = re.findall(patroon1, code)
    matches2 = re.findall(patroon2, kenteken)
    if(len(matches) > 0 and len(matches1) > 0 and len(matches2) > 0):
        break

print("Bedankt nummer in juiste formaat:", matches[0])
print("Bedankt postcode in juiste formaat:", matches1[0])
print("Bedankt kenteken in juiste formaat:", matches2[0])
dontClose = input()
