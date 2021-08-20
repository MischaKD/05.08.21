import tkinter as tk
from pandas import DataFrame  # example of pandas dataframe in matplotlib, embedded in tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use('seaborn')  # nice grid background

data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
         'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]
         }
# df1 = DataFrame(data1, columns=['Country', 'GDP_Per_Capita'])
df1 = DataFrame(data1, columns=[])
print(df1)
# data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
#          'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
#          }
# df2 = DataFrame(data2, columns=['Year', 'Unemployment_Rate'])
#
# data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
#          'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
#          }
# df3 = DataFrame(data3, columns=['Interest_Rate', 'Stock_Index_Price'])
#
# root = tk.Tk()
#
# figure1 = plt.Figure(figsize=(6, 5), dpi=100) # mehrere Figures innerhalb eines einzigen tkinter - mainloops
# ax1 = figure1.add_subplot(111)
#
# bar1 = FigureCanvasTkAgg(figure1, root) # Beispiel fuer mehrere FigureCanvas mit jeweils einem Plot innerhalb eines tkinter-mainloops.
# bar1.get_tk_widget().grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)  # Aehnliches Verhalten erzielbar auch durch Subplots.
# df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()
# df1.plot(kind='bar', legend=True, ax=ax1)
# ax1.set_title('Country Vs. GDP Per Capita')
#
# figure2 = plt.Figure(figsize=(5, 4), dpi=100)
# ax2 = figure2.add_subplot(111)
#
# line2 = FigureCanvasTkAgg(figure2, root) # Beispiel fuer mehrere FigureCanvas mit jeweils einem Plot innerhalb eines tkinter-mainloops.
# line2.get_tk_widget().grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W) # Aehnliches Verhalten erzielbar auch durch Subplots.
#
# df2 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()
# df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
# ax2.set_title('Year Vs. Unemployment Rate')
#
# figure3 = plt.Figure(figsize=(5, 4), dpi=100)
# ax3 = figure3.add_subplot(111)
#
# ax3.scatter(df3['Interest_Rate'], df3['Stock_Index_Price'], color='g')
#
# scatter3 = FigureCanvasTkAgg(figure3, root) # Beispiel fuer mehrere FigureCanvas mit jeweils einem Plot innerhalb eines tkinter-mainloops.
# scatter3.get_tk_widget().grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W) # Aehnliches Verhalten erzielbar auch durch Subplots.
# ax3.legend(['Stock_Index_Price'])
# ax3.set_xlabel('Interest Rate')
# ax3.set_title('Interest Rate Vs. Stock Index Price')
#
# b = tk.Button(root, text="Quit", command=quit)
# b.grid(row=1, column=0, columnspan=3, sticky=tk.N + tk.S + tk.E + tk.W)
#
# root.mainloop()
