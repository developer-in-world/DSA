class Solution:
    def func(self, n, result):
        result.append(n)
        
        if n == 1:
            return result
        if n % 2 == 0:
            return self.func(n//2, result)
        else:
            return self.func(n*3 + 1, result)

solver = Solution()
n = int(input("Enter the number: "))
ans = []
result = solver.func(n, ans)
print(result)