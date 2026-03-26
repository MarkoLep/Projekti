import math
lista = []
while True:
    luku = int(input("Anna luku 0 lopettaa:"))
    lista.append(luku)
    print("Lista nyt:", lista)
    print("Lista järjestyksessä", sorted(lista))
    if luku <= 0:
        print("ohjelma loppuu....")
        break