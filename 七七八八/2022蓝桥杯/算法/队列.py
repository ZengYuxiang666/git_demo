class Queue:
    def __init__(self, size):
        self.queue = [0 for i in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def push(self, element):
        if not self.is_fill():
            self.queue[self.rear] = element
            self.rear = (self.rear + 1) % self.size
        else:
            raise IndexError('Queue is full')

    def pop(self):
        if not self.is_empty():
            element = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return element
        else:
            raise IndexError('Queue is empty')

    def is_empty(self):
        if self.rear != self.front:
            return False
        else:
            return True

    def is_fill(self):
        if (self.rear + 1) % self.size != self.front:
            return False
        else:
            return True
q = Queue(5)
q.push(3)
print(q.queue)