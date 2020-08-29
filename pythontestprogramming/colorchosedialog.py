from tkinter import *

root=Tk()

def callback():
    fileName=colorchooser.askcolor()
    print(fileName)


Button(root,text='颜色选择',command=callback).pack()




mainloop()




#怎么报错了呢
