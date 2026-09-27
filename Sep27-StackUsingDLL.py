class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, value):
        if self.head is None:
            # It is empty stack and this will be the new one
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(value)
            
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
    
    def peekOrTop(self):
        if self.head is None:
            raise IndexError("The Stack is empty to Peek")
        
        return self.tail.value
    
    def pop(self):
        if self.head is None:
            raise IndexError("The stack is empty to Pop")
        
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return
        
        self.tail = self.tail.prev
        self.tail.next = None


stack = DLL()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peekOrTop())
stack.pop()
print(stack.peekOrTop())
stack.pop()
stack.pop()
stack.pop()
