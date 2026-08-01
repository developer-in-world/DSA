class Solution:
    def lowerBound(self,nums,target):
        n = len(nums)
        low , high = 0, n-1
        lb = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid+1

        return lb
    
    def upperBound(self, nums, target):
        n = len(nums)
        ub = n
        low, high = 0, n-1
        
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] > target:
                ub = mid
                high = mid -1
            else:
                low = mid + 1
        return ub

solver = Solution()
arr = list(map(int, input().split()))
target = int(input())
print(solver.upperBound(arr, target))
