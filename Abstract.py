from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0

    @abstractmethod
    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


rec = Rectangle(3, 4)
sq = Square(4)
print("The area of the Rectangle is : ", rec.area())
print("The perimeter of the Rectangle is : ", rec.perimeter())
print("The area of the Square is : ", sq.area())
print("The perimeter of the Square is : ", sq.perimeter())
