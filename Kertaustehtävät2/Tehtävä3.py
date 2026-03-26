lista = ["Marko1","Joonas","kone","sali","maa","kuu","Antero"]
järjestys = 0
for i in lista:
    if len(i) > 5:
        järjestys += 1
print("yli viisikirjaimisia sanoja on:", järjestys)