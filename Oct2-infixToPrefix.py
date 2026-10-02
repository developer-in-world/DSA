class Solution:
    def precedence(self, ch):
        if ch == "+" or ch == "-":
            return 1
        elif ch == "*" or ch == "/":
            return 2
        elif ch == "^":
            return 3
        else:
            return 0

    def infixToPrefix(self, s):

        # reverse the given (string is immutable)
        s = s[::-1]
        s = s.replace("(", "temp").replace(")","(").replace("temp",")")

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
                stack.pop()
            else:
                while stack and self.precedence(stack[-1]) > self.precedence(char): # if both + and - have same powers so we dont pop just add on top it 1 == 1
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        return "".join(result[::-1]) # reversing again at the end


solver = Solution()
expression = input("Enter the expression: ")
result = solver.infixToPrefix(expression)
print(f"Output expression, coverted from in to prefix: {result}")

"""
    Enter the expression: (A+B)*C-D+F
    Output : +-*+ABCDF
    
    Steps to do this are
    1) reverse the given string 
    2) do the infix to postfix conversion, where we stack the symbols with similar precedences
    3) at last reverse the result to get the appriprate result of our own
    
"""
