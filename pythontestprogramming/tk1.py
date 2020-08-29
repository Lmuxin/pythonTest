import tkinter as tk

app=tk.Tk() #窗口
app.title('fish')  #窗口的名字

theLabel=tk.Label(app,text='我的第二个窗口程序!')  #标签,题目
theLabel.pack()#自动调节组件的尺寸位置

app.mainloop() #窗口的阻塞键循环,必须要有,程序才能执行
