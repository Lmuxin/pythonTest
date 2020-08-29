from tkinter import *

root=Tk()

Label(root,text='账号:').grid(row=0,column=0)
Label(root,text='密码:').grid(row=1,column=0)

v1=StringVar()
v2=StringVar()            


e1=Entry(root,textvariable=v1)
e2=Entry(root,textvariable=v2,show="*")
e1.grid(row=0,column=1,padx=10,pady=5)
e1.grid(row=1,column=1,padx=10,pady=5)



def show():
    print("账号:%s" % e1.get())
    print("密码:%s" % e2.get())
    
Button(root,text='芝麻开门',width=10,command=root.quit)\
                                                .grid(row=3,column=0,sticky=E,padx=10,pady=5)
Button(root,text='退出',width=10,command=root.quit)\


mainloop()
  



#tmd哪个地方错了   为什么账号显示不出来文本框,为什么输入密码 不显示*****
