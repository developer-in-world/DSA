class FrontSideStack:
    def __init__(self):
        self.stack = [] # --> [] appending and removing from frontside of arr as the stack

    def isEmptyStack(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.insert(0, value) # this ops give us O(N)

    def pop(self):
        if not self.isEmptyStack(): # O(N)
            return self.stack.pop(0)
        else:
            print("Stack is empty")

    def top(self):
        if not self.isEmptyStack():
            return self.stack[0]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.stack)


class Stack:
    def __init__(self):
        self.stack = [] # the best is to use the this implementation because of O(1) ops in stack using the arr
                        # [] <-- appending and removing from here
    def isEmptyStack(self):
        return len(self.stack) == 0
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.isEmptyStack() != True:
            x = self.stack.pop()
            return x
        else:
            print("The stack is already Empty cant remove out of thin Air")
    
    def top(self):
        if self.isEmptyStack() != True:
            return self.stack[-1]
        else:
            print("Stack is Empty and I cant see the elements out of thin Air")
    
    def size(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(22)
stack.push(100)
print(stack.stack)
print(stack.pop())
print(stack.size())
