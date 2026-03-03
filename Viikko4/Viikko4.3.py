smallest = None
biggest = None
while True:
    luku = input("Anna luku (Enter lopettaa): ")
    if luku == "":
        break
    luku = float(luku)
    if smallest is None:
        smallest = luku
        biggest = luku
    else:
        if luku < smallest:
            smallest = luku
        if luku > biggest:
            biggest = luku
if smallest is not None:
    print("Ohjelma loppuu... pienin ja suurin numero oli", smallest, biggest)
else:
    print("Et antanut yhtään lukua.")
