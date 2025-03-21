from colorpoint import Colorpoint

class AdvancedPoint(Colorpoint):#this means that we are inheriting from Color point
    COLOR = ["red", "green", "blue", "black", "white"]
    def __init__(self, x, y, color):
        if not isinstance(x,(int,float)):
            raise TypeError("x must be a number")
        if not isinstance (y,(int,float)):
            raise TypeError("y must be a number")
        if not color in self.COLOR:
            raise ValueError(f"color must be one of: {self.COLOR}")
        super().__init__(x, y, color) #call the init method of the parent

p = AdvancedPoint(1,2, "red")
print(p)
print(p.distance_orig())
p = AdvancedPoint("Jon","Jeb", "red")
print(p)
p.distance_orig()
