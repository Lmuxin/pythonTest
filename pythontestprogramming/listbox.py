from tkinter import *

master =Tk()



thelb=Listbox(master,selectmode=EXTENDED,height=11)
thelb.pack()
for item in range(11):
   thelb.insert(END,item)







# thelb.delete(1)   删除
mainloop()
