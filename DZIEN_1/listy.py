kraj = ["Polska","Norwegia","Rumunia","Kanada","Portugalia","Chiny"]
print(kraj)
print(kraj[3])
kraj.sort()
print(kraj)
kraj.reverse()
print(kraj)
kraj.sort(reverse=True)
print(kraj)
kraj.append("Brazylia")
print(kraj)
kraj.insert(3,"Turcja")
print(kraj)

# kraj.append(input("podaj nowy kraj... "))
# print(kraj)

kraj.remove("Norwegia")
print(kraj)
print("Laos" in kraj)


pies = ["buldog angielski","labrador","bokser"]
pies_cena = [7000,5000,6100]

sklepzoo = [[pies,"kot","papuga","mysz","szynszyla"],[pies_cena,2300,8700,45,320]]
print(sklepzoo[0])
print(sklepzoo[0][0][0],"kosztuje",sklepzoo[1][0][0],"zł")

rasa = ["pitbull","york","spaniel"]

rasa = rasa + pies
print(rasa)
