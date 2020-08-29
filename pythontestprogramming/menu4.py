from tkinter import *

root=Tk()

def callback():
    print('你好')
    
mb=Menubutton(root, text='点我',relief =RAISED)
mb.pack()

filemenu=Menu(mb,tearoff=False)

filemenu=Menu(mb,tearoff=True)
filemenu.add_command(label='打开',command=callback)
filemenu.add_command(label='保存',command=callback)
filemenu.add_separator()  #分割线
filemenu.add_command(label='退出',command=root.quit)



mb.config(menu=filemenu)


mainloop()
