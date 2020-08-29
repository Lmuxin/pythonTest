from tkinter import *

root=Tk()

text=Text(root,width=30,height=30)

text.pack()

photo=PhotoImage(file="2.jpg")

def show():
      text.imag_create(END,image=photo)
    

b1=Button(text,text='啊哈哈',command=show)
text.window_create(INSERT,window=b1)





mainloop()

