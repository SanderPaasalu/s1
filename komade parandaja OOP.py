import re
from easygui import *
class komad:
    def koma(self):
        file=enterbox("Mis faili soovite parandada?")
        fail=open(file, "r+")
        #küsib mis faili soovitakse avada ja avab selle
        tekst=fail.read()
        fail.close()
        vast=enterbox("Kas tekstis on loendeid?(jah või ei)")
        if vast=="ei":
            tekst=tekst.replace(",","")
        #küsib kas failis on loendeid kui vastus on ei siis võtab ära kõik komad
        tekst=re.sub(r"et",",et",tekst)
        tekst=re.sub(r"aga",",aga",tekst)
        tekst=re.sub(r"kuid",",kuid",tekst)
        tekst=re.sub(r"vaid",",vaid",tekst)
        tekst=re.sub(r"sest",",sest",tekst)
        tekst=re.sub(r"mis",",mis", tekst)
        tekst=re.sub(r"kes",",kes", tekst)
        tekst=re.sub(r"siis",",siis", tekst)
        #paneb iga sõna ette kus kindlalt peab koma olema koma
        msgbox(tekst)
        #näitab milline tekst nüüd välja näeb kuna miks mitte
        with open(file, "w") as filetowrite:
            filetowrite.write(tekst)
    
    
    
    
tekst = komad()    
tekst.koma()    