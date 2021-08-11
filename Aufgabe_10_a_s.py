# Variant 1 with results in Terminal

dateiname = "aufgabe10_a.txt"
a = 1
b = 1
with open(dateiname,"w") as f:
    for i in range(1,101):
        if i < 101:
            d = f"{i:.1f}, {a:.1f}, {b:.1f}\n"
            res = f.write(d)  # Zeilenweises Schreiben am Dateiende (Zeile wird angehaengt)
            print(d, end="")# res = f.write(f"{a},")
            # res = f.write(f"{b}\n")
            # res += f.write("\n")
            a +=2
            b +=3

print(dateiname)
print(f)

# Variant 2 without result in Terminal

dateiname = "aufgabe10_a.txt"
a = 1
b = 1
with open(dateiname,"w") as f:
    for i in range(1,101):
        if i < 101:
            res = f.write(f"{i:.1f}, {a:.1f}, {b:.1f}\n")  # Zeilenweises Schreiben am Dateiende (Zeile wird angehaengt)
            a +=2
            b +=3

print(dateiname)
print(f)

