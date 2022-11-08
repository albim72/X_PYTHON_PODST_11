
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




