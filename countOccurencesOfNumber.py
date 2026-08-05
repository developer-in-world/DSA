class Solution:
    def bruteForce(self, nums, target):
        n = len(nums)
        count = 0
        
        for i in range(n):
            if nums[i] == target:
                count += 1
        
        return count
    
    def bruteForceInspiredfromfirstandlast(self, nums, target):
        n = len(nums)
        first, last = -1, -1
        
        for i in range(n):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        
        return ((last-first) + 1) if first != -1 else 0
    
    def _lowerbound(self, nums, target):
        n = len(nums)
        low, high = 0, n-1
        lb = -1
        
        while (low<=high):
            mid = low + (high-low) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    
    def _upperbound(self, nums, target):
        n = len(nums)
        low, high = 0, n-1
        ub = len(nums)
        
        while (low<=high):
            mid = low + (high-low) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
        
    def optimalSolution(self, nums, target):
        first = self._lowerbound(nums, target)
        last = self._upperbound(nums, target)
        
        if first == -1 or nums[first] != target:
            return 0
        else:
            return last-first
        


solver = Solution()
nums = list(map(int, input().split()))
target = int(input())
result = solver.optimalSolution(nums, target)
print(result)
