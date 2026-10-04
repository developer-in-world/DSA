class Solution:
    def naiveSolution(self, n, arr):
        if n is None or len(arr) == 0:
            return None
        
        expected = (n*(n+1))//2
        actual = 0
        
        for value in arr:
            actual += value
        
        ans = expected - actual
        return ans
    
    def xorSolution(self, n, arr):
        if n is None or len(arr) == 0:
            return None
        
        expected, actual = 0, 0
        
        for i in range(1, n+1):
            expected = expected ^ i
        
        for value in arr:
            actual = actual ^ value
        
        ans = expected ^ actual
        return ans
            
        




n = int(input("Enter the length: "))
nums = list(map(int, input("Enter the values of arr: ").split()))
solver = Solution()
result = solver.xorSolution(n, nums)
print(result)
