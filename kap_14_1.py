# import tkinter                                  # einfache Import-Option
#
# root = tkinter.Tk()                             # root Instanz, "Hauptfenster"
#
# l = tkinter.Label(root,text = "Hello, world!")  # erzeugt Label widget
# l.pack()                                        # Geometriemanager pack()
# root.mainloop()                                 # startet den eventloop.
#
# from tkinter import *                          # alternative Import-Option
#
# root = Tk()
# w = Label(root,text="Hello, world!")
# w.pack()
# root.mainloop()

# import tkinter as tk                          # empfohlene Import-Option
# #
# root = tk.Tk()                                # Instantiierung von Tk
# w = tk.Label(root,text="Hello, world!")       # erzeugt "Label" widget
# w.pack()                                      # Geometriemanager pack()
# # #
# root.mainloop()                               # startet den eventloop.

import tkinter as tk                          # empfohlene Import-Option
#
root = tk.Tk()
f = tk.Frame(root)
f.pack()
w = tk.Label(f,text="Hello, world!")       # erzeugt "Label" widget
w.pack()                                      # Geometriemanager pack()
# #
root.mainloop()                               # startet den eventloop.

test