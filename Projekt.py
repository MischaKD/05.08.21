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
# required bib
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams

fname = " "

class Plotwindow():
    def __init__(self, masterframe, size):
        (w, h) = size
        self.figure = plt.Figure(size)
        self.axes = self.figure.add_subplot(111)
        # create canvas as matplotlib drawing area
        self.canvas = FigureCanvasTkAgg(self.figure, master=masterframe)
        self.canvas.get_tk_widget().grid()  # Get reference to tk_widget

    #        print (self.canvas.get_tk_widget())
    def plotxy(self, x, y):
        self.axes.scatter(x, y)
        self.canvas.draw()

    def clearplot(self):
        self.axes.cla()  # clear axes /clf: clear figure
        self.canvas.draw()


class ReadData():

    def __init__(self):
        self.index = 0  # index of function call

    def piechart(self):
        # read data from csv
        df = pd.read_csv("crowdfunding.csv")
        # print(df.columns) # check the name of the columns
        # print(df)

        # drop column "Unnamed: 0"
        df.drop(columns=['Unnamed: 0'], inplace=True)
        # print(df)
        # print(df.columns) # check the name of the columns

        # Let's have a look how much money was collected by each sector.
        df_sector = df.groupby(['sector']).agg({'funded_amount': 'size'})
        print(df_sector)
        # print(df_sector.columns) # checking columns

        df_sector.reset_index(inplace=True)  # reset index to get all columns
        print(df_sector)
        # print(df_sector.columns)

        label = df_sector['sector']
        sizes = df_sector['funded_amount']
        explode = (0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # exploding  wedges  in a pie chart
        # colors - # to change a color of wedges

        # Matplotlib Pie chart
        fig, ax = plt.subplots(figsize=[10, 10])  # fix the size of plot

        ax.pie(x=sizes,
               labels=label,
               autopct='%1.1f%%'  # shows us the percentage distribution

               , labeldistance=1.07
               # ,rotatelabels=True
               , explode=explode
               , textprops={'fontsize': 12}
               , shadow=True
               , startangle=15

               )

        ax.set_title("Money collected by sectors", fontsize=25, weight="bold", color='blue')

        ax.axis('equal')  # the chart is displayed as a circle

        # Problem
        ax.legend(title="Sectors", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=15, title_fontsize=20)  #

        plt.show()  # to see only the graphics and not the coordinates


def plotdata():
    b3.invoke()
    b3.flash()
    x, y = datrd.piechart()
    plot_w.plotxy(x, y)

def get_data():
    filename.set(filedialog.askopenfilename(initialdir="/Users/Alfa/python", title="Open Data File:",
                 filetypes=(("csv files", "*.csv"), ("all files", "*.*"))))

def clear():
    plot_w.clearplot()


if __name__ == "__main__":  # verhindert Start bei Import; ermöglicht Start bei Ausführung als Executable.
    datrd = ReadData()
    root = tk.Tk()
    root.title("MyPlot")
    filename = tk.StringVar()
    filename.set(" ")
    mainframe = tk.Frame()
    plot_w = Plotwindow(mainframe, (8, 6))
    mainframe.grid(row=1, rowspan=8, column=0)
    buttonframe = tk.Frame()
    buttonframe.grid(row=0, column=0,sticky = tk.W)
    l1 = tk.Label(buttonframe, text="Daten plotten: ")  #
    l1.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    b1 = tk.Button(buttonframe, text="Select", command=get_data)  #
    b1.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
    b2 = tk.Button(buttonframe, text="Plot", command=plotdata)  #
    b2.grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W)
    b3 = tk.Button(buttonframe, text="Clear", command=clear, activeforeground = "red")
    b3.grid(row=0, column=3, sticky=tk.N + tk.S + tk.E + tk.W)
    b4 = tk.Button(buttonframe, text="Close", command=root.destroy)
    b4.grid(row=0, column=4, sticky=tk.N + tk.S + tk.E + tk.W)
    root.mainloop()