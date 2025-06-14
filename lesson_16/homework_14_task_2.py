import math
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def perimeter_calculation(self):
        pass

    @abstractmethod
    def area_calculation(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.__radius = radius

    def perimeter_calculation(self):
        return math.pi * self.__radius * 2

    def area_calculation(self):
        return math.pi * self.__radius ** 2


class Square(Figure):
    def __init__(self, side):
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("Side must be a positive number")
        self.__side = side

    def perimeter_calculation(self):
        return self.__side * 4

    def area_calculation(self):
        return self.__side ** 2


class Rectangle(Figure):
    def __init__(self, side_1, side_2):
        if not all(isinstance(side, (int, float)) and side > 0 for side in [side_1, side_2]):
            raise ValueError("Sides must be positive numbers")
        self.__side_1 = side_1
        self.__side_2 = side_2

    def perimeter_calculation(self):
        return (self.__side_1 + self.__side_2) * 2

    def area_calculation(self):
        return self.__side_1 * self.__side_2

figures = []

def add_figure(figure):
    if not isinstance(figure, (Circle, Square, Rectangle)):
        raise TypeError("Only Circle, Square, or Rectangle instances are allowed")
    figures.append(figure)

add_figure(Circle(2))
add_figure(Square(3))
add_figure(Rectangle(4, 5))

for figure in figures:
    print(f"{figure.__class__.__name__}:")
    print(f"  Perimeter: {figure.perimeter_calculation():.2f}")
    print(f"  Area: {figure.area_calculation():.2f}\n")
