import tkinter as tk             # Uebrtragung von Variablen von eienr Funktion in eine andere Funktion mittels 1. globalen Variablen; 2. tkinter-Variablen.
from tkinter import filedialog   # Im Fall von Klassen zus. Instanz-Variablen sowie generell "mutable" types wie Listen, dicts.

root = tk.Tk()
tk_fname = tk.StringVar()
fname=""

def fileopen():

    global fname
#    root.update()
    fname = filedialog.askopenfilename(filetypes=[("json files","*.json"),("All files","*.*")], initialdir = "C:/users/alfa/python", title = "Select File:")
    print (fname,type(fname))
    tk_fname.set(fname)
#    root.destroy()
#    return fname

def work():
    print("4:",fname)
    print("5:",tk_fname.get())

b = tk.Button(root,text = 'Open File', command = fileopen, bg = "azure4") # # see https://tcl.tk/man/tcl8.6/TkCmd/colors.htm
b.pack(fill= tk.X)
d = tk.Button(root,text = 'show File content', command = work)
d.pack(fill = tk.X)
c = tk.Button(root,text = 'Quit', command = root.quit)
c.pack(fill = tk.X)
#print('1',fname)
root.mainloop()
print("2",fname)
print("3:tk_fname",tk_fname.get())
