from tkinter import *

root=Tk()

#这样是横向填充

Label(root,text='red',bg='red',fg='white').pack(side=LEFT)
Label(root,text='green',bg='green',fg='black').pack(side=LEFT)
Label(root,text='blue',bg='blue',fg='white').pack(side=LEFT)




#这样是向填充

Label(root,text='red',bg='red',fg='white').pack(fill=X)
Label(root,text='green',bg='green',fg='black').pack(fill=X)
Label(root,text='blue',bg='blue',fg='white').pack(fill=X)


mainloop()
