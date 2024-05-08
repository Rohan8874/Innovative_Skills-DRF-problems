import math
class Shape:
    def __init__(self, radius=None, length=None, width=None, base=None, height=None):  
        self.radius = radius
        self.length = length
        self.width = width
        self.base = base
        self.height = height
    def area(self):
        pass
    
class Circle(Shape): 
    def area(self):
        return math.pi* self.radius ** 2
    
class Rectangle(Shape):
    def area(self):
        return self.length * self.width
    
class Triangle(Shape):
    def area(self):
        return 0.5 * self.base * self.height
    
def main(choice):
    if choice=='circle':
        radius = float(input('Enter the redius of the circle: '))
        circle = Circle(radius)
        print('Area of the circle:', circle.area())
    elif choice=='rectangle':
        length = float(input('Enter the length of rectangle: '))
        width = float(input('Enter the width of rectangle: '))
        rectangle = Rectangle(length, width)
        print('Area of rectangle:', rectangle.area())
    elif choice=='triangle':
        base = float(input('Enter the base of triangle: '))
        height = float(input('Enter the height of triangle: '))
        triangle = Triangle(base, height)
        print('Area of triangle:', triangle.area())
    else :
        print('Invalid shape choice!')


choice=input("Enter shape (circle, rectangle, triangle): ")
main(choice)


