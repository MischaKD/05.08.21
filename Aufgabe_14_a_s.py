import tkinter

root = tkinter.Tk()
l = tkinter.Label(root, text = "Hello! This is my first Widget")
l.pack()

but=tkinter.Button(root, text = "Just close this window", command=root.quit)
but.pack()
root.mainloop()






# class Action(tkinter.Frame):
#     def __init__(self, *args, **kwargs):
#         super().__init__(self, *args, **kwargs)
#         self.pack
#         self.widget()
#
#     def widget(self):
#