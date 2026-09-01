class Solution:
    def bruteForce(self, nums):
        result = [[]]
        for num in nums: # this bareBruteForce I thought adding the list with lists to generate new lists
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [num])
            result.extend(new_subsets)
        return result
    
    def optimalSolution(self, nums):
        n = len(nums)
        total_subsets = (1<<n) # using the bit manipluation to solve
        result = []
        for num in range(0, total_subsets):
            lst = []
            for i in range(0, n):
                if num & (1<<i) != 0:
                    lst.append(nums[i])
            result.append(lst)
        return result
                
             
            

solver = Solution()
nums = list(map(int, input().split()))
result = solver.bruteForce(nums)
print(result)
