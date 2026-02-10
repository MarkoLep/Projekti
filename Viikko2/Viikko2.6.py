import random
kolmenkoodi = ""
for i in range(3):
    kolmenkoodi+= str(random.randint(0, 9))
neljankoodi = ""
for i in range(4):
    neljankoodi += str(random.randint(1, 6))
print("Kolminumeroinen koodi:", kolmenkoodi)
print("Nelinumeroinen koodi:", neljankoodi)
