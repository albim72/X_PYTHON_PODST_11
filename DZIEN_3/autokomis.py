from xml.etree.ElementTree import Element,SubElement,Comment
import xml.etree.ElementTree as ET
from prettyfy import pretty

top = Element("autokomis")
auto1 = SubElement(top,'samochod')

id = SubElement(auto1,'id')
id.text = 'sam1'

marka = SubElement(auto1,'marka')
marka.text = 'Subaru'

model = SubElement(auto1,'model')
model.text = 'Impreza'

poj = SubElement(auto1,'pojemnosc')
poj.text = '2.0'

cena = SubElement(auto1,'cena')
cena.text = '55000'

wyp_dod = SubElement(auto1,'wyp_dodatkowe')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czarna perła'

klima = SubElement(wyp_dod,'klimatyzacja')
klima.text = 'RTG446464'

#drugi egzemplarz (samochód)

auto2 = SubElement(top,'samochod')

id = SubElement(auto2,'id')
id.text = 'sam2'

marka = SubElement(auto2,'marka')
marka.text = 'Subaru'

model = SubElement(auto2,'model')
model.text = 'Outback'

poj = SubElement(auto2,'pojemnosc')
poj.text = '2.4'

cena = SubElement(auto2,'cena')
cena.text = '120000'

wyp_dod = SubElement(auto2,'wyp_dodatkowe')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czerwony metallic'

pod = SubElement(wyp_dod,'dodatkowe_pod')
pod.text = '3'

print(pretty(top))

zapis = open("autokomis.xml","a",encoding="utf-8")
zapis.write(pretty(top))
zapis.close()


