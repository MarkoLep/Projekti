def gallonat_litroiksi(maara):
    return maara * 3.785
while True:
    maara = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa): "))
    if maara > 0:
        break
litrat = gallonat_litroiksi(maara)
print(f"{maara} gallonaa = {litrat:.3f} litraa")