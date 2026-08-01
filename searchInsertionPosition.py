class Solution:
    def bruteForce(self, nums, target):
        n = len(nums)
        index = n
        
        for i in range(n):
            if nums[i] >= target:
                index = i
                break
        
        return index
    
    def optimal(self, nums, target):
        n = len(nums)
        lb = n
        low, high = 0, n-1
        
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid -1
            else:
                low = mid+1
        return lb



solver = Solution()
arr = list(map(int, input().split()))
target = int(input())

