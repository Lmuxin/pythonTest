from tkinter import *
root=Tk()


s1=Scale(root,from_=0,to=42,tickinterval=5,resolution=5,length=200).pack()


s2=Scale(root,from_=0,to=200,tickinterval=10,length=600,orient=HORIZONTAL).pack()




mainloop()
