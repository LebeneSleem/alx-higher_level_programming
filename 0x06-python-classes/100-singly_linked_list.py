#!/usr/bin/python3
"""Module for a singly linked list."""


class Node:
    """Defines a node."""

    def __init__(self, data):
        """Initializes the node with instance variables."""
        self.data = data
        self.next_node = None


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes the singly linked list."""
        self.head = None

    def is_empty(self):
        """Checks if the linked list is empty."""
        return self.head is None

    def append(self, data):
        """Appends a new node with the given data to the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        if self.is_empty():
            return "Empty Linked List"
        else:
            elements = []
            current = self.head
            while current:
                elements.append(str(current.data))
                current = current.next_node
            return " -> ".join(elements)
