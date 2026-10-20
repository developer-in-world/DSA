class Solution:
    def next_greater_elements2_optimized(self, arr:list[int]) -> list[int]:
        
        if len(arr) == 0:
            return []
        
        else:
            n = len(arr)
            result = [-1] * n
            monotonic_stack = []
            
            for i in range(2*n-1, -1, -1):
                
                while monotonic_stack and monotonic_stack[-1] <= arr[i%n]:
                    monotonic_stack.pop()
                
                if i < n and monotonic_stack:
                    result[i] = monotonic_stack[-1]
                
                monotonic_stack.append(arr[i%n])
            
            return result


solver = Solution()
nums = list(map(int, input("Enter the arr values: ").split()))
result = solver.next_greater_elements2_optimized(nums)
print(f"Output: {result}")

"""
Enter the arr values: 2 10 12 1 11
Output: [10, 12, -1, 11, 12]

"""
