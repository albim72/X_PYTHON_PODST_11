import json

json_source = '{"imiona":["Jan","Leon","Benedykt"],"nawisko":"Kos","miasto":"Lublin","wiek":40,"umowa_o_prace":"False"}'

print(json_source)
print(type(json_source))

osoba_dict = json.loads(json_source)

print(osoba_dict)
print(type(osoba_dict))
print(osoba_dict["miasto"])
print(osoba_dict["imiona"][0])


autokomis = {
    "marka":"Opel",
    "model":"Insignia",
    "rok":2019,
    "cena":72560.80
}

print(type(autokomis))

jsonauto = json.dumps(autokomis,indent=4)
print(jsonauto)

with open("jsonauto.json","w",encoding="utf-8") as f:
    f.write(jsonauto)

with open("jsonauto.json","r",encoding="utf-8") as f:
    print(f.read())


print("**************************************")

with open("org.json","r",encoding="utf-8") as f:
    org_dict = json.load(f)

print(org_dict)


extra = {
    "id_proj":345345,
    "tematyka":"sztuczna inteligencja",
    "temat":"nowoczesne systemy rekomendacji"
}

org_dict.update(extra)

j_org = json.dumps(org_dict,indent=4)
print(org_dict)



with open("org_ex.json","w",encoding="utf-8") as f:
    f.write(j_org)


