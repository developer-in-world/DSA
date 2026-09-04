class Solution:
    def generateSubsequenceEqualToK(self, nums, target):
        result = []
        subset = []
        self.__solve(nums, target, 0, subset, result)
        return result
    
    def __solve(self, nums, target, index, subset, result):
        if index >= len(nums):
            if sum(subset) == target:
                result.append(subset.copy())
            return
        subset.append(nums[index])
        self.__solve(nums, target, index+1, subset, result)
        subset.pop()
        self.__solve(nums, target, index+1, subset, result)
        
solver = Solution()
arr = list(map(int, input().split()))
target = int(input())
result = solver.generateSubsequenceEqualToK(arr, target)
print(result)
        

        