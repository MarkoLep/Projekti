nimi = input("Kerro nimesi:", )
while nimi != "Joonas":
    annokset = float(input("kuinka monta annosta haluat?:"))
    print("se maksaa", annokset * 5.90, "€")
if nimi == "Joonas":
    print("Seuraava, kiitos!")