from tkinter import *
root=Tk()


sb=Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)  #Y必须是大写的


lb=Listbox(root,yscrollcommand=sb.set)


for i in range(1000):
    lb.insert(END,i)


    
lb.pack(side=LEFT,fill=BOTH)


sb.config(command=lb.yview) //设置垂直滚动 内容如何显示,自动的





mainloop()
