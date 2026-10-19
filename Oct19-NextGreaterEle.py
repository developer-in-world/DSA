class Solution:
    
    def solveBru(self, nums:list[int]) -> list[int]:
        if len(nums) == 0: return None
        else:
            ans = [-1]*len(nums)
            
            for i in range(0, len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        ans[i] = nums[j]
                        break
            
            return ans
        
    def solveOpt(self, nums:list[int]) -> list[int]:
        if len(nums) == 0: return None
        else:
            n = len(nums)
            ans = [-1] * n
            mono_stack = []
            
            for i in range(n-1, -1, -1):
                
                while len(mono_stack) != 0 and mono_stack[-1] <= nums[i]:
                    mono_stack.pop()
                    
                if len(mono_stack) != 0:
                    ans[i] = mono_stack[-1]
                    
                mono_stack.append(nums[i])
            
            return ans


solver = Solution()
nums = list(map(int, input("Input: ").split()))
result = solver.solveOpt(nums)
print(f"Output: {result}")

"""
Input: 19 2 4 9 3 5 8 10
Output: [-1, 4, 9, 10, 5, 8, 10, -1]

"""
