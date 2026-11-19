class Item:
    def __init__(self, value:int, weight:int) -> None:
        self.value = value
        self.weight = weight


class Solution:
    def fractionalKnapsack(self, val:list[int], wt:list[int], capacity:int) -> int:
        
        items = [Item(val[i], wt[i]) for i in range(len(val))]
        items.sort(key=lambda x: x.value / x.weight, reverse=True)
        total_value, currW = 0, 0

        for i in range(len(items)):
            if currW + items[i].weight <= capacity:
                currW += items[i].weight
                total_value += items[i].value
            else:
                remain = capacity - currW
                cost = items[i].value / items[i].weight * remain
                total_value += cost
                break

        return total_value



solver = Solution()
list_vals = list(map(int, input("Enter the values : ").split()))
list_weights = list(map(int, input("Enter the weights : ").split()))
capacity_of_bag = int(input("Enter the weight of the bag : "))
result = solver.fractionalKnapsack(list_vals, list_weights, capacity_of_bag)
print(f"Output : {result}")


