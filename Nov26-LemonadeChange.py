class Solution:
    def lemonade_change(self, bills:list[int]) -> bool:
        n = len(bills)
        canWeSellAll = True
        dollar5, dollar10, dollar20 = 0, 0, 0

        for i in range(n):
            if bills[i] == 5:
                dollar5 += 1

            elif bills[i] == 10:
                if dollar5 >= 1:
                    dollar10 += 1
                    dollar5 -= 1
                else:
                    return False

            else:
                if dollar5 >= 1 and dollar10 >= 1:
                    dollar20 += 1
                    dollar10 -= 1
                    dollar5 -= 1

                elif dollar5 >= 3:
                    dollar20 += 1
                    dollar5 -= 3

                else:
                    return False

        return canWeSellAll


solver = Solution()
arr = list(map(int, input("Enter the dollar bills : ").split()))
result = solver.lemonade_change(arr)
print(f"Output : {result}")

"""
Enter the dollar bills : 5 5 5 10 20
Output : True
"""
