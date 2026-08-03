class Solution:
    def bruteForce(self, nums, target):
        n = len(nums)
        ceil = -1
        floor = -1
        
        for i in range(n):
            if nums[i] <= target:
                floor = nums[i]
                
            if nums[i] >= target:
                ceil = nums[i]
                break
        
        return [floor, ceil]
    
    def optimalSolution(self, nums, target):
        n = len(nums)
        floor, ceil = -1, -1
        low, high = 0, n-1
        
        while low <= high:
            mid = low + (high-low) // 2
            
            if nums[mid] == target:
                return [nums[mid], nums[mid]]
            elif nums[mid] > target:
                ceil = nums[mid]
                high = mid - 1
            else:
                floor = nums[mid]
                low = mid + 1
        
        return [floor, ceil]


solver = Solution()
arr = list(map(int, input().split()))
target = int(input())
result = solver.optimalSolution(arr,target)
print(result)