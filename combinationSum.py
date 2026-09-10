class Solution:
    def solve(self, nums, target, index, total, subset, result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        elif index >= len(nums):
            return
        sum = total + nums[index]
        subset.append(nums[index])
        self.solve(nums, target, index, sum, subset, result)
        
        sum = total
        subset.pop()
        self.solve(nums, target, index+1, sum, subset, result)
        
    def generateCombinationSum(self, nums, target):
        result = []
        self.solve(nums, target, 0, 0, [], result)
        return result
        
        
    
        
        

solver = Solution()
nums = list(map(int, input().split()))
target = int(input())
result = solver.generateCombinationSum(nums, target)
print(result)

