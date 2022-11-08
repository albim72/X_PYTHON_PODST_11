from osoba import Osoba
from pracownik import Pracownik
from student import Student

liczba_wizyt = 0


os1 = Osoba("Jan",45,173,101)
print(f"kolor oczu: {os1.kolor_oczu}")
os1.liczba_wizyt = 5
print(f"liczba wizyt w klubie: {os1.liczba_wizyt}")
print(f"wiek za 10 lat: {os1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os1.czypracownik()})")
print(f"bmi wynosi: {os1.bmi():.2f}, opis: {os1.opis_bmi()}")

print("__________________________________________________")

os2 = Osoba("Ala",30,170,55)
os2.kolor_oczu = "niebieskie"
print(f"kolor oczu: {os2.kolor_oczu}")
os2.print_osoba()
print(f"wiek za 10 lat: {os2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os2.czypracownik()})")

print("__________________________________________________")

pr1 = Pracownik("Olaf",55,176,98,"ABC","dyrektor",10,9800)
pr1.print_osoba()
pr1.print_pracownik()
print(f"wiek za 10 lat: {pr1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({pr1.czypracownik()})")
print(f"bmi wynosi: {pr1.bmi():.2f}, opis: {pr1.opis_bmi()}")

print("__________________________________________________")

st1 = Student("Olaf",22,178,88,34543534,"Automatyka,Elektronika i Informatyka","Informatyka",3)
# st1.wynagrodzenie = 3000
#
# print(f"wynagrodzenie: {st1.wynagrodzenie}")
st1.print_osoba()
st1.print_student()
print(f"wiek za 10 lat: {st1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({st1.czypracownik()})")

print("__________________________________________________")

st2 = Student("Olga",23,170,58,978678,"Budowlany","Budowa mostów",4,"XYZ","sekretarka",1)
# st1.wynagrodzenie = 3000
#
# print(f"wynagrodzenie: {st1.wynagrodzenie}")
st2.print_osoba()
st2.print_student()

st2.print_pracownik()
print(f"wiek za 10 lat: {st2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({st2.czypracownik()})")

#stwórz instancję  klasy student st3 -> student który nie jest pracownikiem, ale jest sportowcem
# wyświetl wszytkie dostępne informacje o tym studencie, korzystając ze stosownych metod!

print("__________________________________________________")

st3 = Student("Tomasz",22,180,77,564545,"Nauk Społecznych","Socjologia",3,dyscyplina="biegi ultra",
              lata_upr=4,best_wynik="102km 19h 12min 4s")
# st1.wynagrodzenie = 3000
#
# print(f"wynagrodzenie: {st1.wynagrodzenie}")
st3.print_osoba()
st3.print_student()
st3.infosport()

print(f"wiek za 10 lat: {st3.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({st3.czypracownik()})")
print(f"bmi wynosi: {st3.bmi():.2f}, opis: {st3.opis_bmi()}")
