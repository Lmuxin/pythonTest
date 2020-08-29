def fbnq(n):
    n1=1
    n2=1
    n3=1

    if n<1 :
        print("有错")
        return -1

        while(n-2)>0:
            n3=n1+n2
            n1=n2
            n2=n3
            n=n-1

        return n3

m=fbnq(20)

if m != -1:
 print(m)

