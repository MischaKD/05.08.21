import tkinter

root = tkinter.Tk()

def readentry():
    v1 = ent1.get()
    print("Hallo: " + v1)
    root.quit()

l = tkinter.Label(root, text="Geben Sie Ihren Namen ein: ")
l.grid(row = 0, column = 0)

but=tkinter.Button(root, text = "Just close this window", command = readentry)
but.grid(row = 2, column = 0, sticky = "nsew")
# but.bind(command=root.quit)

ent1 = tkinter.Entry(root)
ent1.grid(row = 1, column = 0, sticky = "nsew")


root.mainloop()
