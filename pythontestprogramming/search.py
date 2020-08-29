from tkinter import *



root=Tk()


text=Text(root,width=30,height=5)
text.pack()

def getIndex(text,index):
     return tuple(map(int,str.split(text.index(index),'.')))

text.insert(INSERT,'I love fishc.com!')

start='1.0'
while TRUE:
    pos=text.search('o',start,stopindex=END)
    if not pos:
        break
    print('找到了,位置是:',getIndex(text,pos))
    start=pos + '+1c'

mainloop()
