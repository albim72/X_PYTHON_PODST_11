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
