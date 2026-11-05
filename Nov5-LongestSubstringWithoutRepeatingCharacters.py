class Solution:
    def brute_force(self, string:str) -> int:
        maximum_length = 0
        n = len(string)
        for i in range(n):
            my_set = set()
            for j in range(i,n):
                if string[j] in my_set:
                    break
                maximum_length = max(maximum_length, j-i+1)
                my_set.add(string[j])

        return maximum_length

    def optimal_solution(self, string:str) -> int:
        """
        Sliding window and two pointers approach.
        """
        n = len(string)
        my_dict = {}
        maximum_length = 0
        left, right = 0, 0

        while right < n:
            if string[right] in my_dict:
                left = max(left, my_dict[string[right]] + 1)

            maximum_length = max(maximum_length, right-left+1)
            my_dict[string[right]] = right
            right += 1

        return maximum_length



solver = Solution()
string = input("Enter the string: ")
result = solver.optimal_solution(string)
print(f"Output: {result}")

"""
Enter the string: CADBZABCD
Output: 5

"""

