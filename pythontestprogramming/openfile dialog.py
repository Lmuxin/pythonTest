from tkinter import *

root=Tk()

def callback():
    fileName=filedialog.askopenfilename()
    print(fileName)


Button(root,text='打开文件',command=callback).pack()




mainloop()




#怎么报错了呢
