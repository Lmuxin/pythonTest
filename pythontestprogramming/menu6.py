from tkinter import *

OPTIONS=[

       'California','452','ff','wusi','weather']

root=Tk()

variable=StringVar()
variable.set(OPTIONS[0])

w=OptionMenu(root,variable,*OPTIONS)
w.pack()

mainloop()
