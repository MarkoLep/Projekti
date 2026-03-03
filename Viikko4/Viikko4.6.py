import random
N = int(input("Kuinka monta pistettä arvotaan? "))
ympyrassa = 0
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        ympyrassa += 1
pi_likiarvo = 4 * ympyrassa / N
print("Piin likiarvo on:", pi_likiarvo)
