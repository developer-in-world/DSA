class Solution:
    def CombinationSum3(self, k, n):
        result = []
        self.__solve(1, 0, [], k, n, result)
        return result

    def __solve(self, last, total, subset, k, n, result):
        if total == n and len(subset) == k:
            result.append(subset.copy())
            return
        elif total > n or len(subset) > k:
            return
        
        for i in range(last, 10):
            subset.append(i)
            sum = total + i
            self.__solve(i+1, sum, subset, k, n, result)
            subset.pop()

solver = Solution()
k = int(input())
n = int(input())
result = solver.CombinationSum3(k,n)
print(result)