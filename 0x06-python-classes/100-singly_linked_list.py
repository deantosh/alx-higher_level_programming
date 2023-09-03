#!/usr/bin/python3
# author: deantosh daiddoh
"""defines the node os a singly linked list"""


class Node:
    """initializes the node"""
    def __init__(self, data, next_node=None):
        """ node data
            Args:
                data: the node data
                next_node: reference to the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter method"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """sets the data attribute"""
        if not isinstance(self.__data, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gets the next node attribute"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets the next_node attribute value"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""defines a singly linked list"""


class SinglyLinkedList:
    def __init__(self):
        """initialize class"""
        self.head = None

    def __str__(self):
        """makes it printable"""
        pall = ""
        current = self.head
        while (current):
            pall += str(current.data) + "\n"
            current = current.next_node
        return pall[:-1]

    def sorted_insert(self, value):
        """insert in a sorted manner"""
        new = Node(value)
        if not self.head:
            self.head = new
            return

        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return

        current = self.head
        while (current.next_node and current.next_node.data < value):
            current = current.next_node
        if current.next_node:
            new.next_node = current.next_node
        current.next_node = new
