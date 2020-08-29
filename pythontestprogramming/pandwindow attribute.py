from tkinter import *

root=Tk()

def create():
    top=Toplevel()
    top.attributes('-alpha',0.5)
    top.title('fish')


    msg=Message(top,text='i love fishc ')
    msg.pack()


Button(root,text='创建顶级窗口',command=create).pack()



mainloop()
