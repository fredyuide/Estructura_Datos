class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None
