from tkinter import *
import hashlib


root=Tk()


text=Text(root,width=30,height=5)
text.pack()



text.insert(INSERT,'I love fishc.com!')


contents=text.get('1.0',END)

def getsig(contents):
    m=hashlib.md5(contents.encode())
    return m.digest()
    

sig=getsig(contents)


def check():
    contents=text.get('1.0',END)
    if sig !=getsig(contents):
        print("警报,内容变动,后果自负")
    else:
        print('风平浪静')
   


Button(root,text='检查',command=check).pack()

mainloop()

 

