import random
maara = int(input("Montako noppaa heitetään?", ))
summa = 0
for i in range(maara):
    heitto = random.randint(1,6)
    summa += heitto
print("tulosten summa on:", summa)