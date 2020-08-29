from tkinter import *  #导入所有的


def callback():
    var.set('不信')



root=Tk()
frame1=Frame(root)
frame2=Frame(root)

var=StringVar()
var.set('学python\n到Fishc')


#photo=PhotoImage(file='18.gif')  #是一个类
textLabel=Label(frame1,textvariable='学python\n到Fishc',
                           justify=LEFT,
                            image=photo,
                compound=CENTER,
                font=("华康少女字体",20),
                fg='white',
                            padx=10)
textLabel.pack(side=LEFT)


photo=PhotoImage(file='2.jpg')  #是一个类
imgLabel=Label(frame2,image=photo)
imgLabel.pack()


theb=Button(frame2,text='我成年了',command=callback)
mainloop()
