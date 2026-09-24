from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()
        
    def pop(self):
        if len(self.queue) == 0:
            print("Stack is empty")
        else:
            e = self.queue.popleft()
            print(e)
    
    def push(self, value):
        self.queue.append(value)
        n = len(self.queue)
        
        for _ in range(n-1):
            self.queue.append(self.queue.popleft())
    
    def topOrPeek(self):
        if len(self.queue) == 0:
            print("Stack is empty")
        else:
            print(self.queue[0])
    
    def isEmptyStack(self):
        if len(self.queue) == 0:
            return True
        return False
    
    def sizeOfStack(self):
        print(len(self.queue))      


stack = StackUsingQueue()
stack.push(100)
stack.push(200)
stack.push(300)
stack.pop()
stack.topOrPeek()
stack.sizeOfStack()
        
        