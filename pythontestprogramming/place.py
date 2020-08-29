from tkinter import *

root=Tk()

photo=PhotoImage(file="F:\\codephoto\1.gif")
Label(root,image=photo).pack()


def callback():
    print("点到了")

Button(root,text='点点我',command=callback).place(relx=0.5,rely=0.5,anchor=CENTER)

mainloop()
