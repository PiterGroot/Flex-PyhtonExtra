from PIL import Image

afbeelding = Image.open("sunset.png")

afbeelding.show()
breedte = afbeelding.width
hoogte = afbeelding.height

half_breedte = afbeelding.width // 2
half_hoogte = afbeelding.height // 2

nieuwe_afmeting = (half_breedte, half_hoogte)
kleinere_afbeeling = afbeelding.resize(nieuwe_afmeting)
kleinere_afbeeling.save("sunset_klein.png")
