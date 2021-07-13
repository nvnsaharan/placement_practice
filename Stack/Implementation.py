# using Array
class Stack(object):
    def __init__(self):
        self.size = 0
        self.array = []

    def pop(self):
        self.size -= 1
        return self.array.pop()

    def push(self, n):
        self.size += 1
        self.array.append(n)

    def size(self):
        return self.size


# using queue
from queue import Queue


class Stack(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0

    def pop(self):
        self.curr_size -= 1
        return self.q1.dequeue()

    def push(self, n):
        self.curr_size += 1
        while self.q1:
            self.q2.Enqueue(self.q1.dequeue())
        self.q1.Enqueue(n)
        while self.q2:
            self.q1.Enqueue(self.q2.dequeue())

    def size(self):
        return self.curr_size
