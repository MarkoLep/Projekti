Kirjasto = {"Harry Potter": ["Rowling", 1997, "Fiktio"],
            "Aapinen": ["Matti Meikäläinen", 1967, "Opetus"],
            "Sotilaan Käsikirja":["Skabu", 2015, "Opetus"]}
print(Kirjasto["Harry Potter"][0])
print(Kirjasto["Aapinen"][2])
Kirjasto["Sotilaan Käsikirja"][2] = "Koulutus"
Kirjasto["Kirja"] = ["Kirjoittaja",2026, "Genre"]
del Kirjasto["Harry Potter"]
print(Kirjasto)