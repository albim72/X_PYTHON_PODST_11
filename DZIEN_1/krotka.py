animal = ("pies","kot","papuga","pies","lew","krowa","królik","pies")

print(animal)
print(animal.count("pies"))
nm = animal.index("papuga")
print(nm)

if "papuga" in animal:
    print("Tak! papuga to zwierz!")

if "budynek" in animal:
    print("To jest błąd!!!!!!")

anim2 = ("pająk","ryba")

animal = animal + anim2
print(animal)

takiedane = ["obiekt58",56,0.453,True,6,"Zamość",443,0]

print(takiedane)

mojakrotka = tuple(takiedane)
print(mojakrotka)

#zmodyfikuj krokę -> usuń element 56, Zamień "Zamość" na "Toruń", dopisz na końcu krotki 'abc',
#dopisz watość 1 na 5 pozycji.
#pymysł -> zamień krotkę na listę  - funkcja list(), przeprowadź modyfikację ,
# zamień z powrotem listę  na krotkę

mojalista = list(mojakrotka)
mojalista.remove(56)
mojalista.append('abc')
mojalista.insert(5,1)
zm = mojalista.index("Zamość")
mojalista[zm] = "Toruń"

mojakrotka = tuple(mojalista)
print(mojakrotka)

samochod = 'audi','Q7',4.6,34566,2020
marka,model,poj,przebieg,rok = samochod

print(marka)
print(model)
print(poj)
print(przebieg)
print(rok)
