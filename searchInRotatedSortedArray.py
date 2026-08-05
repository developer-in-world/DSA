class Solution:
    def bruteForce(self, nums, target):
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
        return -1
    
    def optimalSolution(self, nums, target):
        n = len(nums)
        low, high = 0, n-1
        
        while(low<=high):
            mid = low +(high-low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1
            
            

solver = Solution()
nums = list(map(int, input().split()))
target = int(input())
result = solver.optimalSolution(nums, target)
print(result)
