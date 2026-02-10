leiviskat = float(input("Leiviskien määrä:", ))
naulat = float(input("Naulojen määrä:", ))
luodit = float(input("luotien määrä:", ))
luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat_yhteensa = luodit_yhteensa * 13.3
kilot = grammat_yhteensa // 1000
grammat = grammat_yhteensa % 1000
print(f"massa nykymitoissa: {kilot} kilogrammaa ja {grammat} grammaa.")
