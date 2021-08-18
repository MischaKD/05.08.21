import tkinter as tk
import tkinter.ttk as ttk
import json
import matplotlib.pyplot as plt
from tkinter import filedialog
from matplotlib.axis import Axis
import matplotlib.patches as mpatches

import numpy as np


# import matplotlib.cm as cm # matplotlib colormaps

def fileopen():

    global fname
#    root.update()
    fname = filedialog.askopenfilename(filetypes=[("json files","*.json"),("All files","*.*")], initialdir = "C:/users/alfa/python", title = "Select File:")
    print (fname,type(fname))
    tk.set(fname)

def myplot(y):
    print(y)
    # Explore the structure of the data.
    filename = r'C:/Users/alarmee/pythonProject/alfakurs/eq_data_1_day_m1.json'
    with open(filename) as f:
        all_eq_data = json.load(f)

    all_eq_dicts = all_eq_data['features']  # enthält den key "Features", der die interesssierenden Daten enthält
    #    print(type(all_eq_dicts[0]))  # Alle Daten aus "Features" sind jetzt in all_eq_dicts.
    #    print(all_eq_dicts[0].keys())
    #    print(all_eq_dicts[0]['geometry']['coordinates'][0])
    #
    mags, plas, lons, lats = [], [], [], []
    for eq_dict in all_eq_dicts:  # all_eq_dicts enthält Liste. Diese kann durchlaufen werden.
        mag = eq_dict['properties']['mag']  #
        pla = eq_dict['properties']['place']  #
        lon = eq_dict['geometry']['coordinates'][0]  # Ausgabe durch Angabe der passenden Keys und "subkeys".
        lat = eq_dict['geometry']['coordinates'][1]
        mags.append(mag)
        plas.append(pla)
        lons.append(lon)
        lats.append(lat)
    #
    smags = [entry * 10 for entry in mags]  # Multiply a List with a constant factor
    # smagm = ["x" if 0<entry<4 else "o" for entry in mags]  # Multiply a List with a constant factor
    # print(smagm)
    fig, ax = plt.subplots()
    # for lo, la, si, sm in zip(lons,lats,smags, smagm):
    #    scatter = ax.scatter(lo,la,s = si, marker = sm)

    sc = scatter = ax.scatter(lons, lats, marker="o", c=mags, s=smags, cmap='plasma_r',
                              label="eqs mag")  # c= CN Farbzyklus ('C0-C9'), colormap 'viridis' or 'viridis_r' for reversed colormap
    # colormap tutorial: https://matplotlib.org/stable/tutorials/colors/colormaps.html
    for i, mag in enumerate(mags):
        if mag >= 4:  # Nur Beschriftung fuer Magnitude ueber 4
            plt.annotate(mag, xy=(lons[i], lats[i]), ha="left", va="bottom", textcoords="offset pixels", xytext=(4, 4),
                         zorder=i, fontsize=8)
            # textcoords = "offset points": Koordinatensystem für xytext, xytext= (4,4) ist der offset in pixel
            # Bedeutung der Parameter: ha = "horizontal Alignment", va = "vertical Alignment",
    cb = fig.colorbar(scatter,
                      ax=ax)  # list of colormaps: https://matplotlib.org/examples/color/colormaps_reference.html
    # cb.set_edgecolor("face") # funktioniert manchmal
    # cb.solids.set_rasterized(True) # nicht immer # legend_elements

    # red_dot = mpatches.Patch(color = "red", label = "eqs magnitude")
    # ax.legend(handles = [red_dot])
    # ax.legend()

    ax.grid()
    plt.minorticks_on()
    ax.set_xlabel("longitude")
    ax.set_ylabel("latitude")
    ax.tick_params(axis="both", which="major", labelsize=12)
    ax.tick_params(axis="both", which="minor", labelsize=10)

    # xticks = np.arange(min(lons), max(lons), 45)  # xticks erzeugen mit numpy "arange" - Funktion, Schrittweite 45
    # ax.set_xticks(xticks)
    plt.show()


root = tk.Tk()
x = 12
y = 20
l1 = tk.Label(root, text="Plotting")
l1.grid(row=0, column=0, sticky=tk.E + tk.W, ipadx=40)  # Ohne ipadx = 40 wird ein 2-spaltiges Gitter erzeugt.
b1 = tk.Button(root, text="Show Plot", command=lambda: myplot(x) if x < 11 else myplot(y))
b1.grid(row=1, column=0, sticky=tk.E + tk.W)
b2 = tk.Button(root, text="Quit", command=root.quit)
b2.grid(row=3, column=0, sticky=tk.E + tk.W)
b3 = tk.Button(root,text = 'Open File', command = fileopen, bg = "azure4")
b3.grid(row=2, column=0, sticky=tk.E + tk.W)

root.mainloop()
