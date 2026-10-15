class Solution:
    def preToPost(self, String):
        stack = []
        
        for char in reversed(String):
            if char.isalnum():
                stack.append(char)
            else:
                # AB
                operand2 = stack.pop() # B
                operand1 = stack.pop() # A
                
                new_exp = f"{operand2}{operand1}{char}"
                stack.append(new_exp)
        
        return stack[-1]
    
solver = Solution()
exp = input("Enter the pre to post expression: ")
result = solver.preToPost(exp)
print(result)
                