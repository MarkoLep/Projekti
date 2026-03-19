luvut = []
syöte = input("Anna luku listaan")
while syöte != "":
    luku =int(syöte)
    luvut.append(luku)
    syöte = input("Anna luku listaan")
luvut.sort(reverse=True)
print("Viisi suurinta lukua on:")
for luku in luvut[:5]:
    print(luku)