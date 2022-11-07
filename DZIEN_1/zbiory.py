drzewa = {"jesion","dąb","buk","jodła","baobab","jabłoń"}
print(drzewa)
print(drzewa)
print(drzewa)
print("____________________")
for d in drzewa:
    print(d)

print("____________________")

print("jesion" in drzewa)
print("osika" in drzewa)

drzewa.add("osika")
print(drzewa)

drzewa.update(["sosna","topola","wierzba"])
print(drzewa)

drzewa.remove("osika")
print(drzewa)

drzewa.discard("jojoba")
print(drzewa)

drzewa.discard("sosna")
print(drzewa)
