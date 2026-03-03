oikea_tunnus = "python"
oikea_salasana = "rules"
vaaria = 0
while vaaria < 5:
    tunnus = input("anna käyttäjätunnus:", )
    salasana = input("anna salasana:", )
    if tunnus == "python" and salasana == "rules":
        print("oikein")
        break
    else: print("väärä salasana")
    vaaria += 1
    tunnus = input("anna käyttäjätunnus:", )
    salasana = input("anna salasana:", )
if vaaria == 5:
    print("pääsy evätty")

