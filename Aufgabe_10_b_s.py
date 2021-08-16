# Variant 1 without reading
# dateiname = "aufgabe10_b.txt"
# a = 1
# b = 1
# with open(dateiname,"w") as f:
#     for i in range(1,101):
#         if i < 101:
#             c = i + a + b
#             res = f.write(f"{i:.1f}, {a:.1f}, {b:.1f}, {c:.1f}\n")  # Zeilenweises Schreiben am Dateiende (Zeile wird angehaengt)
#             a +=2
#             b +=3
#
# print(dateiname)
# print(f)

# Variant 2 with reading

with open("aufgabe10_a.txt","r") as f:
    mylist = []
    for line in f:
        mylist.append(line)
    for i in mylist:
        print(i)

print(mylist) # Liste jetzt vollständig.