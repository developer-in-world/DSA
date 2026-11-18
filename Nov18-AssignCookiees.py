class Solution:
    def solve(self, greed:list[int], cookiees:list[int]) -> int:
        count = 0
        n, m = len(greed), len(cookiees)
        left, right = 0, 0

        greed.sort()
        cookiees.sort()

        while left < n and right < m:
            if greed[left] <= cookiees[right]:
                count += 1
                left += 1
            right += 1

        return count


solver = Solution()
g = list(map(int, input("Enter the greed factor of children : ").split()))
s = list(map(int, input("Enter the cookiee that is there for children : ").split()))
result = solver.solve(g, s)
print(f"Output : {result}")

"""
Enter the greed factor of children : 2 6 8 1 4
Enter the cookiee that is there for children : 4 2 7 1 2 3
Output : 4
"""