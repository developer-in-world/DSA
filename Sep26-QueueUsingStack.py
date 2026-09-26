class QueueUsingStack:
    def __init__(self):
        self.st1 = []
        self.st2 = []
    
    def enqueue(self, value):
        
        while self.st1: # transfer all elements from 1 --> 2
            element = self.st1.pop()
            self.st2.append(element)
        
        self.st1.append(value)
        
        while self.st2: # vice-versa of the first 2 --> 1
            element = self.st2.pop()
            self.st1.append(element)
    
    def isEmptyQueue(self):
        return len(self.st1) == 0 and len(self.st2) == 0
    
    def dequeue(self):
        if self.isEmptyQueue():
            raise IndexError("We cant pop from empty Queue")
        
        return self.st1.pop()
    
    def peekOrTop(self):
        if self.isEmptyQueue():
            raise IndexError("We cant peek into empty Queue")
        
        return self.st1[-1]


queue = QueueUsingStack()

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(30)
print(queue.peekOrTop())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(7)
print(queue.dequeue())
