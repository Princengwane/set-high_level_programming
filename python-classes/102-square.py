#!/usr/bin/python3
"""Defines a comparable Square class."""


class Square:
    """Represents a square, comparable by area."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: the new size.

        Raises:
            TypeError: if value is not an int or a float.
            ValueError: if value is less than 0.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the two areas differ."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this area is smaller."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this area is smaller or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this area is bigger."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this area is bigger or equal."""
        return self.area() >= other.area()
