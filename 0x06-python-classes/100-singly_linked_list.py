#!/usr/bin/python3

"""This module is contains a singly linked list in python
This is an advanced task
"""


class Node():
    """Node class that defines a node
    of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """Initialize class object
        """
        # validating data attribute
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

        # validating next_node attribute
        if next_node is not None and next_node.__class__ is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """Gets the data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data attribute with 'value'
        """
        if not isinstance(value, int):
            raise TypeError("data must be integer")

        self.__data = value

    @property
    def next_node(self):
        """Get next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node
        """
        # validating next_node attribute
        if value is None or value.__class__ == Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """This defines a singly linked list
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        new_node.next_node = self.__head
        self.__head = new_node

    def printList(self):
        data_list = []
        temp = self.__head

        while (temp):
            data_list.append(temp.data)
            temp = temp.next_node
        return sorted(data_list)

    def __str__(self):
        result = self.printList()
        return ('\n'.join(str(i) for i in result))
