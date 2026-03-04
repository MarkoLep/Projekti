palkka = float(input("Tuntipalkkasi:", ))
tunnit = float(input("Tehdyt tunnit:", ))
viikonpaiva = input("viikonpäivä:", )
while viikonpaiva != "sunnuntai":
    print("päiväpalkkasi on", palkka * tunnit, "euroa")
    break
if viikonpaiva == "sunnuntai":
    print("päiväpalkkasi on", palkka * 2 * tunnit, "euroa")