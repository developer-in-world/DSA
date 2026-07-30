from ast import List

class Solution:
    def brute_force(self, nums: List[int], target) -> List[List[int]]:
        result = set()
        n = len(nums)

        if n < 4: return []

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            result.add(tuple(temp))

        return [list(i) for i in result]

    def betterSolution(self, nums: List[int], target) -> List[List[int]]:
        myset = set()
        n = len(nums)

        if n < 4: return []

        for i in range(n):
            for j in range(i+1, n):
                hash_set = set()
                for k in range(j+1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in hash_set:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        myset.add(tuple(temp))
                    hash_set.add(nums[k])

        return [ list(i) for i in myset]

    def optimalSolution(self, nums: List[int], target) -> List[List[int]]:
        n = len(nums)
        if n < 4: return []
        nums.sort()

        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = n - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while l > k and nums[l] == nums[l+1]:
                            l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1

        return result









solve = Solution()
nums = list(map(int, input().split()))
target = int(input())
ans = solve.optimalSolution(nums, target)
print(ans)