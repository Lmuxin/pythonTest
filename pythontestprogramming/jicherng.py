class Turtle:
     def __init__(self,x):
         self.num=x


class Fish:

      def __init__(self,x):
          self.num=x

class Pool:
    
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
    def print(self):
        print('水池里有乌龟%d条,鱼%d条' % (self.turtle.num,self.fish.num))
 
