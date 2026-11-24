class Solution:
    def minimum_number_of_coins(self, arr:list[int], n:int) -> list[int]:
        result = []

        for i in range(len(arr)-1, -1, -1):

            while n >= arr[i]:
                result.append(arr[i])
                n -= arr[i]

        return result
            


solver = Solution()
n = int(input("Enter the N : "))
list_of_coins = list(map(int, input("Enter the list of coins : ").split()))
result = solver.minimum_number_of_coins(list_of_coins, n)
print(f"Output : {result}")

"""
Enter the N : 43
Enter the list of coins : 1 2 5 10 20 50 100 200 500 2000
Output : [20, 20, 2, 1]
"""
