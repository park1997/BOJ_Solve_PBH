class Shape():
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def area():
        return x*y
    
    def perimeter():
        return 2*x+2*y

class Rectangle(Shape):
    x = super.x
    y = super.y
    
    pass

s = Shape(0,0)
print(s.area())