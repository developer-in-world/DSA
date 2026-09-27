class Solution:
    def solve(self, string):
        stack = []
        for bracket in string:
            if bracket == "{" or bracket == "[" or bracket == "(":
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if (ch == "[" and bracket == "]") or (ch == "{" and bracket == "}") or (ch == "(" and bracket == ")"):
                    continue
                else:
                    return False
        return len(stack) == 0
    

solver = Solution()
string = input("Enter the String: ")
result = solver.solve(string)
print(result)