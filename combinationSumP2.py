class Solution:
    def __bruteForceSolve(self, nums, target, index, total, subset, result):
        if total == target:
            sorted_subset = sorted(subset)
            result.add(tuple(sorted_subset))
            return
        elif total > target:
            return
        elif index >= len(nums): # not optimal and throws the TLE error
            return
        
        subset.append(nums[index])
        sum = total + nums[index]
        self.__bruteForceSolve(nums, target, index+1, sum, subset, result)
        
        subset.pop()
        sum = total
        self.__bruteForceSolve(nums, target, index+1, sum, subset, result)
        
    def __OptimalSolutionSolve(self, nums, target, index, total, subset, result):
        n = len(nums)
        if total == 0:
            result.append(subset.copy())
            return
        if total < 0: return
        if index >= n: return
        
        for i in range(index, n):
            if i > index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            sum = total - nums[i]
            self.__OptimalSolutionSolve(nums, target, i+1, sum, subset, result)
            subset.pop()
    
    def generateCombinationSum2(self, nums, target):
        result = []
        nums.sort()
        self.__OptimalSolutionSolve(nums, target, 0, target, [], result)
        return result



solver = Solution()
nums = list(map(int, input().split()))
target = int(input())
result = solver.generateCombinationSum2(nums, target)
print(result)


