while True:
    print("LASKIN")
    print("1 Yhteenlasku")
    print("2 Vähennyslasku")
    print("3 Kertolasku")
    print("4 Jakolasku")
    print("0 Lopeta")
    valinta = input("valitse laskutoiminto:", )
    if valinta == "0":
        print("ohjelma lopetetaan...")
        break
    elif valinta in ["1", "2", "3", "4"]:
        luku1 = float(input("Anna ensimmäinen luku:", ))
        luku2 = float(input("Anna toinen luku:", ))
        if valinta == "1":
            print("tulos on", luku1 + luku2)
        elif valinta == "2":
            print("tulos on", luku1 - luku2)
        elif valinta == "3":
            print("tulos on", luku1 * luku2)
        elif valinta == "4":
            if luku2 == 0:
                print("Ei voi jakaa nollalla")
            else:
                print("tulos on", luku1 / luku2)
    else:
        print("Virheellinen valinta, yritä uudelleen.")