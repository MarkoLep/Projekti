oppilaat = {"Peku": ["Peku", 7, "jalkapallo"],
    "Taneli": ["Taneli", 8, "piirtäminen"],
    "Kartsu": ["Kartsu", 7, "pelaaminen"]}
print(oppilaat["Peku"][1])
print(oppilaat["Taneli"][2])
oppilaat["Kartsu"][2] = "musiikki"
oppilaat["Jonne"] = ["Jonne", 9, "matematiikka"]
del oppilaat["Taneli"]
print(oppilaat)