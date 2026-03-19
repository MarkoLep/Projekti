luku = int(input("Anna kokonaisluku: "))
if luku < 2:
    print("Luku ei ole alkuluku")
else:
    jaollinen = 0
    for i in range(2, luku):
        if luku % i == 0:
            print(f"luku on jaollinen {i}:llä.")
            jaollinen += 1
    if jaollinen == 0:
        print("luku on alkuluku")
    else:
        print("luku ei ole alkuluku")