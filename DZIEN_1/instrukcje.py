a = 1
b = 1

if a>b:
    print("a jest większe niż b")
elif a == 1 and b == 1:
    print("a i b wynoszą jednocześnie 1")
elif a==b:
    print("a jest równe b")
else:
    print("a jest mniejsze niż b")

nr_dnia = 6
match nr_dnia:
    case 1:
        print("poniedziałek")
    case 2:
        print("wtorek")
    case 3:
        print("środa")
    case _:
        print("inny dzień tyogdnia lub pomyłka")


#iteracja - pętla

i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i+=1
else:
    print("ostateczna wartość i:",i)
str_ = "kiwi to jest cierpki owoc"
ow1 = str_.split(" ")
print(ow1)
owoce = [ow1[0],"jabłko","czereśnia","banan","śliwka"]

print(owoce)

for ow in owoce:
    print(ow,end=" ")

print("________________________________________")

cechy = ["kolorowy","elegancki","kosztowny","brudny","przeciętny"]
obiekty = ["płaszcz","przystanek","lampion","budynek","samochód"]

for x in cechy:
    for y in obiekty:
        print(x,y)



