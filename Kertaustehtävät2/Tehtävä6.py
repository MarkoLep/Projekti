def summa(a, b):
    return a + b
def erotus(a, b):
    return a - b
def tulo(a, b):
    return a * b
def jako(a, b):
    if b != 0:
        return a / b
    else:
        return "Ei voi jakaa nollalla"
luku = float(input("Anna eka luku: "))
luku2 = float(input("Anna toka luku: "))
print("Summa:", summa(luku, luku2))
print("Erotus:", erotus(luku, luku2))
print("tulo:", tulo(luku, luku2))
print("Jako:", jako(luku, luku2))