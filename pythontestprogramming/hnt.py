def h(n,x,y,z):
   if n==1:
       print(x,'-->',z)
   else:
        h(n-1,x,z,y) #把前n-1的盘子从x移动到y
        print(x,'-->',z) #把最底下的从x移到z
        h(n-1,y,x,z)#把y上的n-1移动到z
n=int(input("输入盘子数:"))
h(n,'x','y','z')
