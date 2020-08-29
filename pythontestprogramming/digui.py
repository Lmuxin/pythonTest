def f(n):
    if n==1:
     return 1
    else:
     return n*f(n-1)
number=int(input('输入一个整数'))
result=f(number)
print("%d 的阶乘是 %d" %(number,result))
