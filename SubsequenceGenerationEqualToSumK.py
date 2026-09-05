class Solution:
    def generateSubsequenceEqualToK(self, nums, target):
        result = []
        subset = []
        self.__solveOptimal(0, 0, subset, nums, target, result)
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
    
    def __solveOptimal(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        elif index >= len(nums):
            return
        subset.append(nums[index])
        sum = total + nums[index]
        self.__solveOptimal(index+1, sum, subset, nums, target, result)
        e = subset.pop()
        sum = sum - e # this is the optimal solution, where we dont generate all the possible ones and save some computation
        self.__solveOptimal(index+1, sum, subset, nums, target, result)
        
        
solver = Solution()
arr = list(map(int, input().split()))
target = int(input())
result = solver.generateSubsequenceEqualToK(arr, target)
print(result)
        

        