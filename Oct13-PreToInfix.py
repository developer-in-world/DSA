class Solution:
    def preToInfix(self, string):
        stack = []

        for char in reversed(string):
            if char.isalnum():
                stack.append(char)

            else:
                # N,M (inside stack)
                operand1 = stack.pop() # M
                operand2 = stack.pop() # N

                new_exp = f"({operand1}{char}{operand2})"
                stack.append(new_exp)

        return stack[-1]

solver = Solution()
exp = input("Enter the expression for pre to infix: ")
result = solver.preToInfix(exp)
print(result)

"""
The ouput if program ran

Enter the expression for pre to infix: *+PQ-MN (Input)
((P+Q)*(M-N))  (Output)

"""
