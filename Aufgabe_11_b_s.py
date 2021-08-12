import matplotlib.pyplot as plt
import numpy as np

spalte1 = []
spalte2 = []
spalte3 = []
dateiname = "aufgabe10_a.txt"
with open (dateiname) as f: # Datei öffnen (Lesen-modus voreingestellt)
    for line in f:
        # print(line, end="")
        l = line.rstrip("\n").split(",")
        # print(l)
        x = float(l[0])
        y = float(l[1])
        z = float(l[2])
        spalte1.append(x)
        spalte2.append(y)
        spalte3.append(z)
# print(spalte1)
# print()
# print(spalte2)
# print()
# print(spalte3)

#plt.subplot(111)
fig = plt.figure(figsize=(18.0, 9.0))
plt.plot(spalte1, spalte2, "^r", label="data")  # einfacher Plot mit marker "o" linestyle "-" colour "red"
plt.ylabel("spalte2")                                  # y-Achsenbeschriftung erzeugen
plt.xlabel("spalte1")
plt.title("Aufgabe_11_b_s")
# plt.show()
# fig2 = plt.figure(figsize=(10.0, 5.0))
plt.plot(spalte1, spalte3, "o-b", label="data")
plt.ylabel("spalte3")
plt.xlabel("spalte1")
plt.title("Aufgabe_11_a_s")
#plt.xticks([1.0,2.0, 3.0])
# plt.grid()
# hier koennen weitere Formatbefehle folgen
plt.legend()                                                 # legend benötigt "label" bei "plt.plot"
plt.show()

