class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class QueueDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def front(self):
        if self.head is None:
            raise IndexError("The Queue is empty")
        else:
            return self.head.value
    
    def rear(self):
        if self.head is None:
            raise IndexError("The Queue is empty")
        else:
            return self.tail.value
        
    def enqueue(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        
        else:
            newNode = Node(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
    
    def dequeue(self):
        if self.head is None:
            raise IndexError("Queue is empty")
        else:
            if self.head is self.tail:
                self.head = None
                self.tail = None
                return
            
            self.head = self.head.next
            self.head.prev = None



queue = QueueDLL()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(7)
print(queue.front())
print(queue.rear())
queue.dequeue()
queue.dequeue()
print(queue.front())
print(queue.rear())
