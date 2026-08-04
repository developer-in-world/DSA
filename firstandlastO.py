class Solution:
    def bruteForce(self, nums, target):
        n = len(nums)
        first, last = -1, -1
        
        for i in range(n):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
            elif first != -1:
                break
        
        return [first, last]
    
    def _upperbound(self, nums, target):
        n = len(nums)
        low, high = 0, n-1
        ub = -1
        
        while (low <= high):
            mid = low + (high - low) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        
        if ub == -1:
            return len(nums)
        else:
            return ub
    
    def _lowerbound(self, nums, target):
        n = len(nums)
        low, high = 0, n-1
        lb = -1
        
        while(low <= high):
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return lb
    
    def optimalSolution(self, nums, target):
        n = len(nums)
        first = self._lowerbound(nums,target)
        last = self._upperbound(nums, target)
        
        if first == -1 or nums[first] != target:
            return [-1, -1]
        else:
            return [first, last-1]
        
        
        
        
                



solver = Solution()
nums = list(map(int, input().split()))
target = int(input())

result = solver.optimalSolution(nums, target)
print(result)