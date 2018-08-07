class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self)

    def empty(self):
        return self.size() == 0