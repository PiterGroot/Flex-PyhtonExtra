from PIL import Image, ImageFont, ImageDraw
import os
os.system("cls")
print("Welkom gebruiker! Dit is de meme maker 2000 \n")
template = input("Sleep een meme template in deze map en typ de naam + bestandstype (bijv. lol.png , hehe.jpg) hier >>>> ")
print("")
saveName = input("Hoe wil je jouw meme bestandsnaam noemen? >>>> ")


achtergrond = Image.open(template)

breedte = achtergrond.width
hoogte = achtergrond.height

font = ImageFont.truetype("impact.ttf", 60)

tekengebied = ImageDraw.Draw(achtergrond)
regel1 = input("Wat voor tekst wil je op regel 1? >>> ")
regel2 = input("Wat voor tekst wil je op regel 2? >>> ")
tekst =(regel1 + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + regel2)
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=font)
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))
tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2
tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=font, fill=(0,0,0))
tekengebied.multiline_text((tekst_x-3, tekst_y-3), tekst, font=font, fill=(255,255,255))

achtergrond.show()
achtergrond.save(saveName + ".jpg")
