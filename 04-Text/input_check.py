import re



while True:
    nummer = input("Voer je mobiele nummer in >>>> ")

    patroon = "^06-?\d{8}"
    
    matches = re.findall(patroon, nummer)
    if(len(matches) > 0):
        break

print("Bedankt nummer in juiste formaat:", matches[0])

dontClose = input()
