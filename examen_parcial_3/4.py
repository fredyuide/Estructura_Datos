class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.head.value

    def display(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print("Queue:", " -> ".join(map(str, values)))

# Caso de uso práctico
dq = DoublyLinkedQueue()
dq.enqueue(10)
dq.enqueue(20)
dq.enqueue(30)
dq.display()
print("Dequeue:", dq.dequeue())
dq.display()
print("Peek:", dq.peek())
