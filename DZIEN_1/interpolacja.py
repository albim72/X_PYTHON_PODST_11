wiek = 37
miasto = "Lublin"
imie = "Paweł"


osoba = "imię pacjenta: {}, miasto pochodzenia: {}, wiek pacjenta: {}"
print(osoba.format(imie,miasto,wiek))

osoba = "imię pacjenta: {0}, wiek pacjenta: {2}, miasto pochodzenia: {1}"
print(osoba.format(imie,miasto,wiek))

#f-string

print(f"Dane pacjenta -> miasto pochodzenia: {miasto}, imię pacjenta: {imie}, wiek pacjenta: {wiek}")

id_biletu = 564575
miejsce = 4,12
cena = 145.886

koncert = 'nr seryjny biletu: %i, rząd: %i, miejsce: %i, cena biletu: %.2f zł, ' \
          'cena po rabacie 12 proc: %.2f zł' \
          %(id_biletu,miejsce[0],miejsce[1],cena,0.88*cena)
print(koncert)

