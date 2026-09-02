class Solution:
    def Answer(self, nums):
        n = len(nums)
        if n == 0:
            return None
        first, second = float("-inf") , float("-inf")
        for i in range(n):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif nums[i] > second and nums[i] != first:
                second = nums[i]
        return second


nums = list(map(int, input().split()))
solver = Solution()
result = solver.Answer(nums)
print(result)