from PIL import Image, ImageFont, ImageDraw
import io

bestand = open("TextInput.txt", "r")
tekst_regel = bestand.readline()


def makeMeme(string, string1):
    achtergrond = Image.open("meme_template.jpg")

    breedte = achtergrond.width
    hoogte = achtergrond.height

    font = ImageFont.truetype("impact.ttf", 60)

    tekengebied = ImageDraw.Draw(achtergrond)
    tekst = "Coding in Pyhton \n\n\n\n\n\n\n\n\n\n\n\n\n\n No problemo!"
    tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=font)
    print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))
    tekst_x = (breedte - tekst_breedte) / 2
    tekst_y = (hoogte - tekst_hoogte) / 2
    tekengebied.multiline_text((tekst_x, tekst_y), string, font=font, fill=(0,0,0))
    tekengebied.multiline_text((tekst_x-3, tekst_y-3), string1, font=font, fill=(255,255,255))

    achtergrond.show()
    achtergrond.save("meme_met_tekst.jpg")

for x in range(2):
    tekst_regel = tekst_regel.strip()
    makeMeme(tekst_regel, tekst_regel)
    inhoud = tekst_regel
    tekst_regel = bestand.readline()
