class Solution:
    def bruteForce(self, nums:list[int]) -> list[int]:
        if len(nums) == 0:
            return []
        
        i = 0
        while i < len(nums)-1:
            if nums[i] > 0 and nums[i+1] < 0:
                if abs(nums[i]) > abs(nums[i+1]):
                    nums.pop(i+1)
                elif abs(nums[i]) < abs(nums[i+1]):
                    nums.pop(i)
                    if i > 0:
                        i -= 1
                elif abs(nums[i]) == abs(nums[i+1]):
                    nums.pop(i+1)
                    nums.pop(i)
                    if i > 0:
                        i -= 1
            else:
                i += 1
            
        return nums
    
    def optimal(self, nums:list[int]) -> list[int]:
        n = len(nums)
        if n == 0:
            return []
        stack = []
        
        for i in range(n):
            if nums[i] > 0:
                stack.append(nums[i])
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(nums[i]):
                    stack.pop()
                if stack and stack[-1] == abs(nums[i]):
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(nums[i])
        
        return stack
    

solver = Solution()
nums = list(map(int, input("Enter the values of arr: ").split()))
result = solver.optimal(nums)
print(result)

                         
                    
            
        