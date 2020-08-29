def m(n):
    result=n
    for i in range(1,n):      
         result*=i
    return result


number=int(input('Enter your input: '))

result=m(number)
print("%d的阶乘是:%d"   %(number,result))
    
