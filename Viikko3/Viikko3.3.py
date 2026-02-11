sukupuoli = input("Sukupuolesi:", )
hemoglobiiniarvo = float(input("Hemoglobiarvo g/l:", ))
if sukupuoli == "Nainen" and 117 <= hemoglobiiniarvo <= 175:
    print("Hemoglobiinisi on normaali")
elif sukupuoli == "Nainen" and hemoglobiiniarvo > 175:
    print("Hemoglobiinisi on korkea")
elif sukupuoli == "Nainen" and hemoglobiiniarvo < 117:
    print("Hemoglobiinisi on matala")

if sukupuoli == "Mies" and 134 <= hemoglobiiniarvo <= 195:
    print("Hemoglobiinisi on normaali")
elif sukupuoli == "Mies" and hemoglobiiniarvo > 195:
    print("Hemoglobiinisi on korkea")
elif sukupuoli == "Mies" and hemoglobiiniarvo < 134:
    print("Hemoglobiinisi on matala")