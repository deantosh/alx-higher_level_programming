#!/usr/bin/python3
"""defines a square"""


class Square:
    """creates a square"""
    def __init__(self, size=0, position=(0, 0)):
        """intializes the data
           Args:
                size: the length  of side of square
                position: location of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """returns the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)

    @property
    def position(self):
        """gets the position attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the position attribute"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 possitive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """prints the square at a specific position"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("{}".format("\n"), end="")
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print("{}".format(" "), end="")
                for i in range(self.__size):
                    print("{}".format("#"), end="")
                print()
