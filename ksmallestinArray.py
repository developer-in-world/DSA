class Solution:
    def bruteForce(self, nums, left, right, k):
        n = len(nums)

        if not 0 <= left <= right < n:
            return "Invalid Input"

        range_size = right - left + 1

        if not 1 <= k <= range_size:
            return "Invalid Input"

        temp_list = nums[left:right + 1]
        temp_list.sort()

        return temp_list[k - 1]


n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

q = int(input())

solver = Solution()

for i in range(q):
    left = int(input())
    right = int(input())
    k = int(input())

    result = solver.bruteForce(arr, left, right, k)

    print(f"The answer of the smallest is {result}")