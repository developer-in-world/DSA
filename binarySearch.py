class Solution:
    def binarySearchIterative(self, nums, target):
        n = len(nums)
        low, high = 0, n-1

        while low <= high:
            mid = low + (high-low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def recursiveBS(self, nums, target, low, high):
        if low > high: return -1

        mid = low + (high-low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.recursiveBS(nums, target, mid+1, high)
        else:
            return self.recursiveBS(nums, target,low, mid-1)

solver = Solution()
arr = list(map(int, input().split()))
target = int(input())
result = solver.recursiveBS(arr, target,0,8)
print(result)