from tkinter import *

root=Tk()


GIRLS=['西施','貂蝉','王昭君','杨玉环']  #列表

v=[]  #列表  是个变量

for girl in GIRLS:
    v.append(IntVar())
    b=Checkbutton(root,text=girl,variable=v[-1])
    b.pack(anchor=W)
    


mainloop()
