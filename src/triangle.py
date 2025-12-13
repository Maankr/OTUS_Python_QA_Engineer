from figure import Figure
import math

class Triangle(Figure):
   
    def __init__(self,side_a: int | float, side_b: int | float, side_c: int | float):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
           raise ValueError("Triangle sides must be more than 0 ")
      
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
           raise ValueError("The sum of the lengths of the two sides of the triangle must be greater than the third side.")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return (self.side_a + self.side_b + self.side_c)
   
    @property
    def area(self):
        p = self.perimeter / 2
        return math.sqrt(p*((p-self.side_a)*(p-self.side_b)*(p-self.side_c)))
    
