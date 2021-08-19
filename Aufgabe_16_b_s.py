import tkinter as tk
import json
#import matplotlib
#matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import filedialog, simpledialog, messagebox, colorchooser
from matplotlib.axis import Axis
import matplotlib.patches as mpatches
import csv
from datetime import datetime
import matplotlib.dates as mdates

class Plotwindow:
    def __init__(self, masterframe, size):
#        (w, h) = size
        self.figure = plt.Figure(size)
        self.axes = self.figure.add_subplot(111)
        # create canvas as matplotlib drawing area
        self.canvas = FigureCanvasTkAgg(self.figure, master=masterframe)
        self.canvas.get_tk_widget().grid()  # Get reference to tk_widget

    def plotxy(self, x, y):
        self.axes.scatter(x, y,color = "red",marker = "^")
        self.canvas.draw()

    def clearplot(self):
        self.axes.cla()  # clear axes
        self.canvas.draw()

#        b2.config(background = "blue",foreground = "white") # use .config for single or multiple assignments
#        b2["background"]="blue"                             # use [" "] = ... for single assignments

class ReadData:
    def __init__(self):
#        self.index = 0  # index of function call
        pass

    def myscat(self):
        filename = 'C:/Users/alarmee/pythonProject/alfakurs/eq_data_1_day_m1.json'  # anpassen an lokalen Pfad erforderlich
        with open(filename) as f:
            all_eq_data = json.load(f)
        all_eq_dicts = all_eq_data['features']
        mags, plas, lons, lats = [], [], [], []
        for eq_dict in all_eq_dicts:
            mag = eq_dict['properties']['mag']
            pla = eq_dict['properties']['place']
            lon = eq_dict['geometry']['coordinates'][0]
            lat = eq_dict['geometry']['coordinates'][1]
            mags.append(mag)
            plas.append(pla)
            lons.append(lon)
            lats.append(lat)
        return mags, lats


def plotdata():#
    b2.invoke()
    b2.flash()
#    b2.config(bg = "green",state = "disabled")
#    b2["state"]="disabled"
#    print(b2.keys())
    x, y = datrd.myscat()
    plot_w.plotxy(x, y)


def clear():
    plot_w.clearplot()


def fileopen():

    global fname
#    root.update()
    fname = filedialog.askopenfilename(filetypes=[("csv files","*.csv"), ("json files","*.json"),("All files","*.*")], initialdir = "C:/users/alfa/python", title = "Select File:")
    print (fname,type(fname))
    tk_fname.set(fname)


def myplot(y):
    print(y)
    # Explore the structure of the data.
    # filename = r'C:/Users/alarmee/pythonProject/alfakurs/eq_data_1_day_m1.json'
    with open(fname) as f:
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

def fileopen_csv():

    global fname
#    root.update()
    fname = filedialog.askopenfilename(filetypes=[("csv files","*.csv"),("All files","*.*")], initialdir = "C:/users/alfa/python", title = "Select File:")
    print (fname,type(fname))
    tk_fname.set(fname)

def readcsv():

    with open(fname, newline= "") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        #    print(csv_reader)
        line_count = 0
        x, y = [], []
        #     rowlist = []
        Titelzeile = next(csv_reader)
        print(
            f'Spaltenueberschriften sind: {",".join(Titelzeile)}')  # unterschiedliche Anfuehrungszeichen-typen erforderlich
        y_lab = Titelzeile[3]  # Read column title
        for row in csv_reader:
            #        print(row)
            date = datetime.strptime(row[2], "%Y%m%d")
            #        print(date,type(date))
            x.append(date)
            y.append(float(row[3]))
            line_count += 1
    print(f"Processed {line_count} lines.")

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.ylabel("°C")
    plt.title("Tageshoechstwerte")
    plt.plot(x, y, label=y_lab)  # Set Legend entry to column title, then plot
    #
    # res = input("Detailed x-axis? (y/N)")
    #
    # if res == "y":
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))  #
    #    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))   # Die Methode "gca()" bedeutet
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=150))  # "Get current axis".
    #     plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))     #
    plt.gca().xaxis.set_minor_locator(mdates.MonthLocator(interval=1))  #
    fig.autofmt_xdate(
        rotation=30)  # rotate labels to not overlap          # https://matplotlib.org/stable/api/dates_api.html?highlight=daylocator
    #
    plt.legend()
    plt.grid()
    plt.show()
#print("__name__:", __name__)

#if __name__ == "__main__":  # verhindert Start bei Import; ermöglicht Start bei Ausführung als Executable.

root = tk.Tk()
root.title("MyPlot")
tk_fname = tk.StringVar()
fname=""
x = 12
y = 20
mainframe = tk.Frame(root)
mainframe.grid(row=1, column=0)
datrd = ReadData() # Instantiierung der Klasse ReadData
plot_w = Plotwindow(mainframe, (8, 6))  # inch
buttonframe = tk.Frame(root)
buttonframe.grid(row=0, column=0, sticky=tk.N + tk.W)
b1 = tk.Button(buttonframe, text="Plot", command = plotdata, activebackground="red")
b1.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

b2 = tk.Button(buttonframe, text="Clear", command = clear, activebackground="red")
b2.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

#b2.config(activeforeground="red")
b3 = tk.Button(buttonframe, text = "Close", command = root.destroy, activebackground="red")
b3.grid(row=0, column=6, sticky=tk.N + tk.S + tk.E + tk.W)

b4 = tk.Button(buttonframe, text="Read file", command = fileopen)
b4.grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

b5 = tk.Button(buttonframe, text="Open json read file", command=lambda: myplot(x) if x < 11 else myplot(y))
b5.grid(row=0, column=3, sticky=tk.N + tk.S + tk.E + tk.W)

# b6 = tk.Button(buttonframe, text="Read .csv file", command = fileopen_csv)
# b6.grid(row=0, column=5, sticky=tk.N + tk.S + tk.E + tk.W)

b7 = tk.Button(buttonframe, text="Open csv read file", command = readcsv)
b7.grid(row=0, column=4, sticky=tk.N + tk.S + tk.E + tk.W)

root.mainloop()