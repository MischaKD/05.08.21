import tkinter as tk
from pandas import DataFrame  # example of pandas dataframe in matplotlib, embedded in tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams
from tkinter import filedialog, simpledialog, messagebox, colorchooser
import os.path
import tkinter.ttk as ttk
import matplotlib.patches as mpatches

# plt.style.use('seaborn')  # nice grid background


### read data from csv
df = pd.read_csv("crowdfunding.csv")
# print(df.columns) # check the name of the columns
# print(df) # print df

df.drop(columns=['Unnamed: 0'], inplace=True)  # drop column "Unnamed: 0"
# print(df.columns) # check the name of the columns


### Tkinter. Creating an application window
root = tk.Tk()
root.title("Crowd Funding Database")



figure1 = plt.Figure(figsize=(8, 7), dpi=100) # mehrere Figures innerhalb eines einzigen tkinter - mainloops
ax1 = figure1.add_subplot(111)

bar1 = FigureCanvasTkAgg(figure1, root) # Beispiel fuer mehrere FigureCanvas mit jeweils einem Plot innerhalb eines tkinter-mainloops.
bar1.get_tk_widget().grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)  # Aehnliches Verhalten erzielbar auch durch Subplots.

# Let's have a look how much money was collected by each sector.
df_sector = df.groupby(['sector']).agg({'funded_amount': 'size'})
# print(df_sector)
# print(df_sector.columns) # checking columns

df_sector.reset_index(inplace=True)  # reset index to get all columns
# print(df_sector)
# print(df_sector.columns)

label = df_sector['sector']
sizes = df_sector['funded_amount']
explode = (0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # exploding  wedges  in a pie chart
# colors - # to change a color of wedges

# Matplotlib Pie chart

ax1.pie(x=sizes,
       labels=label,
       autopct='%1.1f%%'  # shows us the percentage distribution

       , labeldistance=1.07
       # ,rotatelabels=True
       , explode=explode
       , textprops={'fontsize': 8}
       , shadow=True
       , startangle=15)

ax1.set_title("Money collected by sectors", fontsize=20, weight="bold")
ax1.legend(["Sectors"])

# ax1.axis('equal')  # the chart is displayed as a circle
# ax1.legend(title="Sectors", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=15, title_fontsize=20) #
# plt.show
# plt.show()  # to see only the graphics



#Seaborn.barplot
# why some sectors collected a lot of money, was it a big investment or a lot of people had interest in this sector

figure2 = plt.Figure(figsize=(8, 7), dpi=100)
ax2 = figure2.add_subplot(111)

line2 = FigureCanvasTkAgg(figure2, root) # Beispiel fuer mehrere FigureCanvas mit jeweils einem Plot innerhalb eines tkinter-mainloops.
line2.get_tk_widget().grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W) # Aehnliches Verhalten erzielbar auch durch Subplots.

df_ppl = df.groupby(['sector']).agg({'lender_count': 'size'})
df_ppl.reset_index(inplace=True)  # reset index to get all columns

sns.set_theme(style="whitegrid")
sns.barplot(x="lender_count"
                 ,y="sector"
                 ,data=df_ppl
                 ,palette="nipy_spectral"
                 ,saturation=.7
                 ,order=df_ppl.sort_values('lender_count', ascending = False).sector, ax=ax2)

# set labels
ax2.set_xlabel("Number of Lenders", size=16, weight="bold", color = 'blue')
ax2.set_ylabel("Sector", size=17, weight="bold", color = 'blue')
ax2.set_title("Lender pro Sector", fontsize=20, weight="bold")
# ax2.tick_params(labelsize=13)

# class Application(tk.Frame):  # Klasse "erbt" von "Frame" Klasse
#     def __init__(self, master=None, **options):
#         tk.Frame.__init__(self, master, **options)  # Init Methode der Elternklasse "Frame"
#         self.pack()  # Erforderlich zur Darstellung
#         self.createWidgets()

def say_hello():
    print("hello")

    # def createWidgets(self):
    #     self.Button1 = tk.Button(self, text = 'Button 1', command = self.say_hello, activeforeground = "red")  # erzeugt button1
    #     self.Button1.pack()

fname=""
def fileopen():
    global fname
    fname = filedialog.askopenfilename(filetypes=[("csv files","*.csv"),("All files","*.*")], initialdir = "C:/users/alfa/python", title = "Select File:")
    print (fname,type(fname))

def myplot():
    if os.path.exists(fname):
        with open(fname) as f:
            print("a")
    else:
        res = messagebox.showwarning("please choose the file csv", "Dies ist eine Warning-MessageBox")

### Buttons
b1 = tk.Button(root, text="Quit", command=quit,  bg = "azure4")
b1.grid(row=3, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

b2 = tk.Button(root, text="Plot", command=myplot)
b2.grid(row=2, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

b3 = tk.Button(root,text = 'Open File', command = fileopen)
b3.grid(row=2, column=0, sticky=tk.E + tk.W)


# root.geometry("1000x800+300+250")
root.mainloop()  ### Tkinter. Closing an application window
