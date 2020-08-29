from tkinter import *

root=Tk()
group=LabelFrame(root,text='最好的编程语言是?',padx=5,pady=5)
group.pack(padx=10,pady=10)

Langs=[('python',1),('c',2),('java',3),('c++',4)]

v=IntVar()

v.set(1)

for  lang,num in Langs:
    b=Radiobutton(root,text=lang,variable=v,value=num)
    b.pack(fill=X)



mainloop()
