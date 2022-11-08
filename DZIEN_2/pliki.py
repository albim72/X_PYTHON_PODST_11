import os

f = open("dane.txt","r",encoding="utf-8")
print(f.readline())
print(f.readline())
f.seek(0)
print(f.readline())
print(f.readline())
f.close()
print("_______________________________________________")
f = open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()
print(f.closed)
print("_______________________________________________")
f = open("dane.txt","r",encoding="utf-8")
for linia in f:
    print(linia)
f.close()
print(f.closed)

g = open("message.txt","a",encoding="utf-8")
g.write("to jest ważna wiadmość\n")
g.close()
print("_____________________________________________")
g = open("message.txt","r",encoding="utf-8")
print(g.read())
g.close()

print("_____________________________________________")

if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("plik został usunięty!")
else:
    print("plik nie istnieje!")
