#!/usr/bin/python3
"""Defines a Node class and a SinglyLinkedList class."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data: the integer held by the node.
            next_node: the next node in the list, or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value: the new data.

        Raises:
            TypeError: if value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value: a Node object or None.

        Raises:
            TypeError: if value is neither None nor a Node.
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize a new empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node in the list, keeping it sorted increasingly.

        Args:
            value: the integer to insert.
        """
        new = Node(value)
        if self.__head is None or self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while (current.next_node is not None and
                current.next_node.data <= value):
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new

    def __str__(self):
        """Return the whole list, one node value per line."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
