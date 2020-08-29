import tkinter as tk
class App :
    def __init__(self,master):
        frame=tk.Frame(master)   #框架
        frame.pack(side=tk.LEFT,padx=10,pady=10)


        self.hi_there=tk.Button(frame,text="打招呼",bg='black',fg='white',command=self.sayhi)    #搞了一个按钮 按钮按下时 调用sayh函数,背景是black  字体颜色是whitez
        self.hi_there.pack()

    def sayhi(self):
        print('我是小甲鱼')



root=tk.Tk()
app=App(root)

root.mainloop()
