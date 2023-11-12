# Write a simple python program which define the class, object, inheritance, polymorphism,
# encapsulation and data abstraction.

# Parent Class
class Shape:
    def __init__(self):
        pass

    def area(self):
        pass


# Child Class
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Child Class
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


def get_shape_area(shape):
    return shape.area()


# Encapsulation
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Polymorphism
print("Area of Rectangle: ", get_shape_area(rectangle))
print("Area of Circle: ", get_shape_area(circle))


# Inheritance
class ColoredShape(Shape):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def get_color(self):
        return self.color


# Data Abstraction
red_circle = ColoredShape('red')
print("Color of red circle: ", red_circle.get_color())