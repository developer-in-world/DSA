class Solution:
    def bruteForce(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
    
    def optimalSolution(self, nums, target):
        n = len(nums)
        hashmap = {}
        for i in range(n):
            remaining = target - nums[i]
            if remaining in hashmap:
                return [hashmap[remaining], i]
            hashmap[nums[i]] = i
    

nums = list(map(int, input().split()))
target = int(input())
solver = Solution()
result = solver.optimalSolution(nums, target)
print(result)