class Solution:
    def bruteForce(self, nums):
        result = []
        self.__solveB(nums, 0, [], result)
        return result
        
    def __solveB(self, nums, index, subset, result):
        if index >= len(nums):
            result.append(sum(subset.copy()))
            return
        
        subset.append(nums[index])
        self.__solveB(nums, index+1, subset, result)
        
        subset.pop()
        self.__solveB(nums, index+1, subset, result)
    
    def optimal(self, nums):
        result = []
        self.__solveO(nums, 0, 0, result)
        return result
    
    def __solveO(self, nums, index, total, result):
        if index >= len(nums):
            result.append(total)
            return
        
        sum = total + nums[index]
        self.__solveO(nums, index+1, sum, result)
        
        sum = total
        self.__solveO(nums, index+1, sum, result)

solver = Solution()
nums = list(map(int, input().split()))
result = solver.optimal(nums)
print(result)        