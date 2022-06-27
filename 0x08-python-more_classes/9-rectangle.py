#!/usr/bin/python3
"""
This module defines the a Rectangle class and has 13 functions
"""


class Rectangle:
    """Retangle class that has getters setters properties str and repr methods, a static method and class methods
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Function initializes width and height of the rectangle"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """Function prints out the rectangle in a certain format"""
        stringer = ""
        if self.__height == 0 or self.width == 0:
            return total
        for i in range(self.__height):
            stringer += ("#" * self.__width)
            if i is not self.__height - 1:
                stringer += "\n"
        return stringer

    def __repr__(self):
        """This function return a string representation of the rectangle to be able to recreate a new instance by using eval()"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """This function retrives the private width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """The width value and type are tested in this function"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value



    @property
    def height(self):
        """This function retrives the private height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """The height value and type are tested in this function"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Function returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Fuction returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __del__(self):
        """Function prints message after rectangle is deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Fuction compares two rectangles using a static method"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
