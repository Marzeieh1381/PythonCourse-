class Circle:
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def area(self):
    
        return 3.14* (self.r**2)
        
    def circumference(self):
        
        return 2 * 3.14 * self.r
    
mynewcircle= Circle(2, 3, 5)
    

    
print("area is :" ,mynewcircle.area() )
print( "circumference is :" , mynewcircle.circumference() ) 