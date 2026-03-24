def poista_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]
luvut = [10, 6, 5, 3, 2, 6, 7]
karsittu = poista_parittomat(luvut)
print("Alkuperäinen lista:", luvut)
print("Karsittu lista (vain parilliset):", karsittu)