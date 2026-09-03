class Solution:
    def generateSubSequences(self, nums):
        result = [] 
        subset = [] 
        self.__solve(nums, 0, subset, result) 
        return result
    
    def __solve(self, nums, index, subset, result):
        if index >= len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[index])
        self.__solve(nums, index+1, subset, result)
        subset.pop()
        self.__solve(nums, index+1, subset, result)
        
nums = list(map(int, input().split()))
solver = Solution()
result = solver.generateSubSequences(nums)
print(result)
        