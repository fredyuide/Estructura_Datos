from queue import PriorityQueue

class PriorityQueueWithAI(PriorityQueue):
    def __init__(self):
        super().__init__()

    def enqueue(self, item, priority):
        self.put((priority, item))

    def dequeue(self):
        return self.get()

