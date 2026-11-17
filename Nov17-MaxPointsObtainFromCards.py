class Solution:
    def solve(self, nums:list[int], k:int) -> int:
        n = len(nums)
        if n == k:
            return sum(nums)

        left_sum, right_sum = 0, 0

        for i in range(0, k):
            left_sum += nums[i]

        maxi = left_sum
        right_indx = n - 1

        for i in range(k-1, -1, -1):
            left_sum -= nums[i]
            right_sum += nums[right_indx]
            maxi = max(maxi, left_sum + right_sum)
            right_indx -= 1

        return maxi

solver = Solution()
nums = list(map(int, input("Enter the cards : ").split()))
k = int(input("Enter the value of k: "))
result = solver.solve(nums, k)
print(f"Output : {result}")


"""
Enter the cards : 1 2 3 4 5 6 1
Enter the value of k: 3
Output : 12
"""

