class Solution:
    """In this question we have a sorted and rotated array with the duplicate
    elements in them [6,7,8,1,2,3,4,5], we have to return True or False as the bool."""

    def bruteForce(self, nums, target):
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return True
        return False
    
    
    def optimalSolution(self, nums, target):
        n = len(nums)
        low, high = 0, n-1
        
        while(low<=high):
            mid = low + (high-low) // 2
            
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
                
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
        
        return False
    
    
    
solver = Solution()
nums = list(map(int, input().split()))
target = int(input())
result = solver.optimalSolution(nums, target)
print(result)