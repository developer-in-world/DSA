class Solution:
    def posToPre(self, String):
        stack = []
        
        for char in String:
            if char.isalnum():
                stack.append(char)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                new_exp = f"{char}{operand1}{operand2}"
                stack.append(new_exp)
        
        return stack[-1]

solver = Solution()
exp = input("Enter the pos to pre expression: ")
result = solver.posToPre(exp)
print(result)

""" 
Sample IO

Enter the pos to pre expression: AB-DE+F*/  (Input)
/-AB*+DEF (Output)
"""
