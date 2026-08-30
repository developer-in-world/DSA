class Solution:
    def bruteForce(self, nums):
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                return nums[i]
    
    def bruteForce2(self, nums):
        n = len(nums)
        
        for i in range(n):
            found = False
            for j in range(n):
                if i!=j and nums[i] == nums[j]:
                    found = True
                    break
            if found == False:
                return nums[i] # Both the bruteForces are same (but Slightly different thinking logic from my side)
                
    def optimalSolution(self, nums):
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans        
                
    
    
nums = list(map(int, input().split()))
solver = Solution()
result = solver.optimalSolution(nums)
print(result)
