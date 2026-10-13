class Solution:
    def postToInfix(self, string):
        stack = []
        
        for char in string:
            if char.isalnum():
                stack.append(char)
                
            else:
                # AB
                operand2 = stack.pop() # B
                operand1 = stack.pop() # A
                
                new_exp = f"({operand1}{char}{operand2})"
                
                stack.append(new_exp)
                 
        return stack[-1] # only one will be left out which is answer use -1 or 0 both are the same
    

solver = Solution()
exp = input("Enter the expression for post to infix: ")
result = solver.postToInfix(exp)
print(result)
    