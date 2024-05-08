class AllShape:
       
    def calculate_circle_area(self,radius):
        return 3.1416 * radius ** 2
    
    def calculate_rectangle_area(self, length, width):
        return length * width
    
    def calculate_triangle_area(self, base, height):
        return 0.5 * base * height

class AllArea(AllShape):
    def __init__(self,choice) :
        self.choice=choice
    def area(self):
        if self.choice=='circle':
            radius = float(input('Enter the redius of the circle: '))
            print('Areal of the circle:',super().calculate_circle_area(radius))
        elif self.choice=='rectangle':
            length = float(input('Enter the length of rectangle: '))
            width = float(input('Enter the width of rectangle: '))
            print('Area of rectangle:',super().calculate_rectangle_area(length,width))
        elif self.choice=='triangle':
            base = float(input('Enter the base of triangle: '))
            height = float(input('Enter the height of triangle: '))
            print('Area of triangle:',super().calculate_triangle_area(base,height))
        else :
            print('Invalid shape choice!')

choice=input("Enter the shape of(circle, rectangle, triangle): ")
all_shape=AllArea(choice)
all_shape.area()
