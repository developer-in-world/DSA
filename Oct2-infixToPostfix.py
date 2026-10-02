class Solution:
    def precedence (self, ch):
        if ch == "+" or ch == "-":
            return 1
        elif ch == "*" or ch =="/":
            return 2
        elif ch == "^":
            return 3
        else:
            return 0
    
    def infixToPostfix(self, s):
        stack = []
        result = []
        
        for char in s:
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()       # ()
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)
            
        while stack:
            result.append(stack.pop())
        
        return "".join(result)


solver = Solution()
expression = input("Enter the expression: ")
result = solver.infixToPostfix(expression)
print(f"Output expression, coverted from in to postfix: {result}")

"""
    Enter the expression: a+b*(c^d-e)
    Output : abcd^e-*+
    
"""
