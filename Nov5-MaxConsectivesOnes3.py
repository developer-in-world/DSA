class Solution:
    def brute_force(self, arr:list[int], k:int) -> int:
        n = len(arr)
        maxi = 0

        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if arr[j] == 0:
                    zeros += 1
                if zeros > k:
                    break

                maxi = max(maxi, j-i+1)

        return maxi

    def better_solution(self, arr:list[int], k:int) -> int:
        n = len(arr)
        maxi = 0
        left, right = 0, 0
        zeros = 0

        while right < n:
            if arr[right] == 0:
                zeros += 1
            while zeros > k:
                if arr[left] == 0:
                    zeros -= 1
                left += 1

            # if zeros <= k:
            #     maxi = max(maxi, right-left+1) it works the same because the above while will make sure we get only the valid pairs and doesnt need checking again

            maxi = max(maxi, right-left+1)   
            right += 1

        return maxi

    def optimal_solution(self, arr:list[int], k:int) -> int:
        n = len(arr)
        left, right = 0, 0
        zeros = 0
        maxi = 0

        while right < n:
            if arr[right] == 0:
                zeros += 1
            if zeros > k:
                if arr[left] == 0:
                    zeros -= 1
                left += 1

            if zeros <= k:
                maxi = max(maxi, right-left+1)
            right += 1

        return maxi




solver = Solution()
input_list = list(map(int, input("Enter the list of 1's and 0's : ").split()))
k = int(input("Enter the value of k (number): "))
result = solver.optimal_solution(input_list, k)
print(f"Output : {result}")




"""
Enter the list of 1's and 0's : 1 1 1 0 0 0 1 1 1 1 0 
Enter the value of k (number): 2
Output : 6


Better Solution: Uses a sliding window with two pointers. Expands the window using `right` and shrinks it using `left` until the number of zeros becomes valid (at most k). Updates the maximum window length after every valid window.

Time Complexity: O(N)
Space Complexity: O(1)

Optimal Solution: Uses the same sliding window technique but shrinks the window only once using `if` instead of `while`. Updates the maximum length only when the current window is valid. The window may temporarily remain invalid, but the maximum length is maintained correctly.

Time Complexity: O(N)
Space Complexity: O(1)
"""


    



