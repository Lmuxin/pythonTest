from tkinter import *
root=Tk()




def callback(event):
    print("点击位置:",event.x,event.y)


frame=Frame(root,width=200,height=20)
frame.bind('<Button-1>',callback)                     #鼠标点击事件 1是左键 2是中间 3是右键
frame.pack()


mainloop()
