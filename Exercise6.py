# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = math.pi * self.radius**2
        return a

    def perimeter(self):
        p = 2 * math.pi * self.radius
        return p

c1 = Circle(78)
print('Area of circle:', c1.area())
print('perimeter of circle:', c1.perimeter())