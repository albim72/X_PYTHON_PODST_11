
print("kilka ważnych funckji")
def witaj():
    print("witaj nowy użytkowniku")
    print("opłać abonament")
    print("zaloguj się!")

witaj()

#wykonaj 250 razy funkcję witaj....
#przy kązdym wykonaniu podaj nr wykonania

# for i in range(250):
#     print(f"_______ wykonanie nr {i+1} ___________")
#     witaj()


#funkcja 2

def obywatel(nrtelefonu,kraj="Polska"):
    return f"Kraj pochodzenia: {kraj}, numer telefonu: {nrtelefonu}"

print(obywatel(53454534,"Etiopia"))
print(obywatel(67645634543,"Kanada"))
print(obywatel(76867573453446,"Japonia"))
print(obywatel(75674564))

#funkcja 3

def fx(m):
    if m == 2:
        return 22
    else:
        return m**3

def oblicz(a,c,v):
    __n = (a+c)*v+fx(c)
    return __n

print(oblicz(3,2,7))


#funkcja 4

def miasta(miasto3,miasto2="Zamość",miasto1="Kraków"):
    print(f"miasto tygodnia: {miasto1}, drugie miejsce: {miasto2}, trzecie miejsce: {miasto3}")

miasta("Katowice","Kielce","Koszalin")
miasta("Katowice","Kielce")
miasta("Katowice")

miasta("Gdańsk","Lublin","Warszawa")

#wypisz ranking miast zadając pozycje: miasto1, miasto3 natomiast miasto2 pozostaw domyślne

miasta("Tarnów",None,"Toruń")
miasta("Tarnów",miasto1="Toruń")
miasta(miasto1="Toruń",miasto3="Poznań")


#funckja 5

def zamki(id,*zamek,kupon):
    print(f"zamek tygodnia: {zamek[0]} cena wejścia niższa o {kupon} zł, drugie miejsce: {zamek[1]}, trzecie miejsce: {zamek[2]}")

zamki(1,"Malbork","Ogrodzieniec","Czersk",kupon=20)
zamki(2,"Janowiec","Malbork","Będzin","Ogrodzieniec","Czersk","Chojnik",kupon=5)

zm = ["Malbork","Ogrodzieniec","Czersk"]
zamki(3,zm,"x","y",kupon=6)



