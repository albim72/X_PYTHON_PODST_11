print("to jest pierwsza linia kodu...")

a = 7
print(a)
print(type(a))

a = "siódemka"
print(a)
print(type(a))

d:float
d= 1.1

print(d)
print(type(d))

d = True
print(d)
print(type(d))

#komentarz w Pythonie
"""
komentarz dokumentacyjny 
wieloliniowy
"""

#skrót CTRL+D -> powielenie linii lub bloku
#skrót CTRL + / -> komentowanie/odkomentowanie bloku kodu

pr1 = "pora roku: jesień"
pr2 = "pora roku: zima"
rok = 2022

print(pr1+", a następna "+pr2+", rok:"+str(rok))
print(pr1,"a następna",pr2,"rok",rok,sep=" - ")

y = 11.678

print(5*y)

x = "7.9"
print(12*x)

print(eval(x)*12)
print(float(x)*12)

g1 = 10
g2 = 11

print(g1+g2,g1-g2,g1*g2,g1/g2,g1%g2,g1**g2, sep=" @@ ")

w = g1/g2
print(type(w))

print(round(10.67))
print(round(10.6767655354,3))

print(pow(3,4))

i = 9
i+=3 #i=i+1

print(i)

kr = "lajkonik"

print(kr)
#teskt jest trakowany przez Pythona jak lista z indeksami od 0
print(kr[0])
print(kr[1])
print(kr[2:6])
print(kr[3:])
print(kr[:5])
print(kr[-1])
print(kr[-2])



