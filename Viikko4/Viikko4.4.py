import random
oikee = random.randint(1, 10)
while True:
    vastaus = float(input("Anna luku:", ))
    if vastaus > oikee:
        print("Arvasit liian ison numeron")
    elif vastaus < oikee:
        print("Arvasit liian pienen numeron")
    else:
        print("Arvasit oikein")
        break