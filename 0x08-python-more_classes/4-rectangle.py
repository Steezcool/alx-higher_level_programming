#!/usr/bin/python3
# 4-rectangle.py
""" it defines class Rectangle"""


class Rectangle:
    """it represents rectangle"""
    def __init__(self, width=0, height=0):
        """it initializes an instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """it gets the width of rectangle"""
        return (self.__width)
    @width.setter
    def width(self, value):
        """it sets the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """it gets the height of a rctangle"""
        return (self.__height)
    @height.setter
    def height(self, value):
        """it sets the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
    @property
    def height(self):
        """it gets height of a rectangle"""
        return (self.__height)
    @height.setter
    def height(self, value):
        """it sets the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """it returns rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """it returns perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """it prints rectangle with #"""
        rect_shape = []
        
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            [rect_shape.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect_shape.append("\n")
        return ("".join(rect_shape))

    def __repr__(self):
        """Returns strin rep of rectangle"""
        rect_shape = "Rectangle(" + str(self.__width)
        rect_shape += ", " + str(self.__height) + ")"
        return (rect_shape)
