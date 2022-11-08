from osoba import Osoba

os1 = Osoba("Jan",45,173,101)
print(f"kolor oczu: {os1.kolor_oczu}")
os1.print_osoba()
print(f"wiek za 10 lat: {os1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os1.czypracownik()})")

print("__________________________________________________")

os2 = Osoba("Ala",30,170,55)
os2.kolor_oczu = "niebieskie"
print(f"kolor oczu: {os2.kolor_oczu}")
os2.print_osoba()
print(f"wiek za 10 lat: {os2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os2.czypracownik()})")
