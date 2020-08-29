class Countlist:
    def __init__(self,*args):#长度不确定,定义可变的
        self.values=[x for x in args]
        self.count={}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self,key):
        self.count[key]+=1
        return self.values[key]
    
        
