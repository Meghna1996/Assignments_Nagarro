import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius
    def perimeter(self):
        return 2 * pi * radius
    def __eq__(self,other):
        return self.radius == other.radius
    def __le__(self,other):
        return self.radius <= other.radius
    def __ge__(self,other):
        return self.radius >= other.radius
    def __ne__(self,other):
        return self.radius != other.radius
    def __lt__(self,other):
        return self.radius < other.radius
    def __gt__(self,other):
        return self.radius > other.radius


c = Circle(3)
c2= Circle(4)
print(c.area())
print(c == c2)
print(c <= c2)
print(c >= c2)
print(c < c2)
print(c > c2)
print(c != c2)