from ast import List

class Solution:
    def brute_force(self, nums: List[int], target) -> List[List[int]]:
        result = set()
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            result.add(tuple(temp))

        return [list(i) for i in result]


solve = Solution()
nums = list(map(int, input().split()))
target = int(input())
ans = solve.brute_force(nums, target)
print(ans)