from tkinter import *
root=Tk()




def callback(event):
    print(event.char)
    
    
frame=Frame(root,width=200,height=200)
frame.bind('<Key>',callback)                    #键盘事件
frame.focus_set()             
frame.pack()


mainloop()
