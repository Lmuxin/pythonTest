try:

    f=open('wo.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错'+str(reason))
