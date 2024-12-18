class StackArray:
    def __init__(self, capacity=100):
        self.stack = []
        self.capacity = capacity

    def push(self, value):
        if len(self.stack) >= self.capacity:
            raise OverflowError("Stack overflow")
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
