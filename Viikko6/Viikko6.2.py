import random
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)
tahkot = int(input("Kuinka monta tahkoa nopassa on?: "))
while True:
    tulos = heita_noppaa(tahkot)
    print(tulos)
    if tulos == tahkot:
        break