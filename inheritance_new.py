import math
class Frame:
    def __init__(self):
        pass
    def range(self):
        pass
    
class Circle(Frame):
    def __init__(self, radius):
        self.radius = radius
    
    def range(self):
        return math.pi * self.radius ** 2

class Rectangle(Frame):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def range(self):
        return self.length * self.width
    
class Triangle(Frame):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def range(self):
        return 0.5 * self.base * self.height
    
def main():
    frame = input("Enter Frame (Circle, Rectangle, Triangle): ").lower()
    
    if frame == "circle":
        radius = float(input("Enter Radious: "))
        circle = Circle(radius)
        print("Range:", circle.range())
       
    elif frame == "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        rectangle = Rectangle(length, width)
        print("Range:", rectangle.range())
        
    elif frame == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        triangle = Triangle(base, height)
        print("Range", triangle.range())
        
    else:
        print("Invalid Range")
        
if __name__ == "__main__":
    main()
        