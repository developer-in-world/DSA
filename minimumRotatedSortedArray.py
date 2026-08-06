class Solution:
    def bruteForce(self, nums):
        n = len(nums)
        minimum = float("inf")
        
        for i in range(n):
            minimum = min(minimum, nums[i])
        
        return minimum
    
    def optimalSolution(self, nums):
        n = len(nums)
        minimum = float("inf")
        low, high = 0, n-1
        
        while(low<=high):
            mid = low + (high-low) // 2
            if nums[mid] <= nums[high]:
                minimum = min(minimum, nums[mid])
                high = mid - 1
            else:
                minimum = min(minimum, nums[low])
                low = mid + 1
        return minimum
                

solver = Solution()
nums = list(map(int, input().split()))
result = solver.optimalSolution(nums)
print(result)
