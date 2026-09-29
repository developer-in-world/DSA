class MinStack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def pop(self):
        if self.isEmpty():
            print("The Stack is Empty")
            return -1
        else:
            e = self.stack.pop()
            return e
    
    def push(self, value):
        self.stack.append(value)
    
    def top(self):
        if self.isEmpty():
            print("Nothing is there to see in it")
            return -1
        else:
            return self.stack[-1]
    
    def getminN(self):
        # Big O(N)
        if self.isEmpty():
            print("Stack empty")
            return -1
        else:
            minimum = float("inf")
            for i in self.stack:
                if i < minimum:
                    minimum = i
            return minimum


stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.getminN())


# The below is the logic where the ops are done in O(1) no need to search the using the loop

"""
class MinStack:
    def __init__(self):
        self.stack = []  

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([value, value])
        else:
            mini = min(self.stack[-1][1], value)
            self.stack.append([value, mini])
        
    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            e = self.stack.pop()
            return e[0]
        
    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][0]  

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]      
"""
