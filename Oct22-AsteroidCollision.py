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
    

solver = Solution()
nums = list(map(int, input("Enter the values of arr: ").split()))
result = solver.bruteForce(nums)
print(result)

                         
                    
            
        