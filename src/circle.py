from figure import Figure
import math

class Circle(Figure):

    def __init__(self, radius: int | float):
        if radius <= 0:
            raise ValueError("Radius must be more than 0")
        self.radius = radius
    
    @property
    def perimeter(self):
        return (2 * math.pi * self.radius)
    
    @property
    def area(self):
        return (math.pi * (self.radius**2))
    