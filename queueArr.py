class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            raise ValueError("The queue is empty")

    def rear(self):
        if not self.isEmpty():
            return self.queue[-1]
        else:
            raise ValueError("The queue is empty")

    def dequeue(self):
        if not self.isEmpty():
            x = self.queue.pop(0)
            return x
        else:
            raise ValueError("Cannot dequeue from an empty queue")

    def enqueue(self, value):
        self.queue.append(value)


class OppositeDirectionQueue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.isEmpty():
            return self.queue[-1]
        else:
            raise ValueError("The queue is empty")

    def rear(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            raise ValueError("The queue is empty")

    def dequeue(self):
        if not self.isEmpty():
            x = self.queue.pop()
            return x
        else:
            raise ValueError("Cannot dequeue from an empty queue")

    def enqueue(self, value):
        self.queue.insert(0, value)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.size())
print(queue.front())
print(queue.rear())
print(queue.dequeue())
print(queue.dequeue())
print(queue.front())
print(queue.rear())
print(queue.isEmpty())
