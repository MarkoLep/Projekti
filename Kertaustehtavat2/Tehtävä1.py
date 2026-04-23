ihmiset = {"John":["John", 30, "engineer"],
"Emily":["Emily", 25, "artist"],
"Anna":["Anna", 22, "student"]}
print(ihmiset["John"][0],ihmiset["John"][1], ihmiset["Emily"][2])
ihmiset["Anna"][2] = "teacher"
ihmiset["James"] = ["James", 28, "Writer"]
ihmiset["Sophia"] = ["Sophia", 35,"Doctor"]
del ihmiset["Sophia"]
print(ihmiset)
