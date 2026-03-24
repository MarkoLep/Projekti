def laske_summa(luvut):
    return sum(luvut)
luku = input("Anna luvut: ")
luvut = list(map(int, luku.split()))
summa = laske_summa(luvut)
print("Listan summa on:", summa)