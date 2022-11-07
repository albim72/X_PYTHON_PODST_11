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

litery = ['a','b','c','d','e','f','g','h']

print('przed zmianą',litery)

litery[2:7] = [99,23,58]

print('po zmianie',litery)

litery_m = litery
litery_p = list(litery)
litery_q = litery[:]

print('przed zmianą',litery)
print('przed zmianą',litery_m)

litery[:] = [1002,1004,1119,1145]

print('po zmianie',litery)
print('po zmianie',litery_m)
print('po zmianie',litery_p)
print('po zmianie',litery_q)
