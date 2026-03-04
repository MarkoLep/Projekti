import math
from math import sqrt
while True:
    luku = int(input("anna kokonaisluku:", ))
    if luku == 0:
        print("exiting.....")
        break
    elif luku < 0:
        print("virheellinen numero")
    else:
        print("luvun neljöjuuri on", (sqrt(luku)))

