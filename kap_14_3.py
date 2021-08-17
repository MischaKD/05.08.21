import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
label = tk.Label(root, text="Name")
# label.pack(fill = tk.BOTH, expand = 1)  # .pack () in der Zeile des Erstellens ist meist problematisch
label.pack()
ent = tk.Entry(root,fg = "green", bg = "yellow")
ent.pack(fill = tk.BOTH, expand = 1)  # besser ist eine neue Zeile mit label.pack() und ent.pack()
but = tk.Button(root, text="Quit", command=root.quit)
but.pack(fill = tk.BOTH, expand = 1)

#root.geometry("400x400")
root.mainloop()
