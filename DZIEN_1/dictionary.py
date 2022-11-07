#słownik -> <dict> => (klucz, wartość)

sam = {
    "marka":"Ford",
    "model":"Mustang",
    "rocznik":1972,
    "przebieg":560900
}

print(sam)
m = sam["przebieg"]
print(m)

m = sam.get("przebieg")
print(m)

sam["rocznik"] = 2018
sam["przebieg"] = 45600

print(sam)

sam["poj"]=4.4
print(sam)

sam.update({"cena":123000,"salon":"Ford USA Kraków"})

print(sam)

print(sam.items())
print(sam.keys())
print(sam.values())

print("_____________klucze________________")

for x in sam:
    print(x,end=" ")

print("\n_____________wartości - I sposób________________")
for y in sam:
    print(sam[y], end=" ")

print("\n_____________wartości - II sposób________________")
for x in sam.values():
    print(x,end=" ")

print("\n_____________wartości - parami________________")
for x,y in sam.items():
    print(x,":",y)


autokomis = {
    "sam1":{
            "marka":"Ford",
            "model":"Mustang",
            "rocznik":1972,
            "przebieg":560900
    },
    "sam2":{
            "marka":"Opel",
            "model":"Insignia",
            "rocznik":2016,
            "przebieg":89070
    },
    "sam3":{
            "marka":"Jeep",
            "model":"Cherokee",
            "rocznik":2010,
            "przebieg":187000
    }

}

print(autokomis)

print(autokomis["sam3"])
print(autokomis["sam3"]["marka"])
