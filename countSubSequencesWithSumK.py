class Solution:
    def countSubSequencesWithSumK(self, arr, target):
        count = self.backTrack(0, 0, arr, target)
        return count
    
    def backTrack(self, index, total, arr, target):
        if total == target:
            return 1
        elif total > target: return 0 
        elif index >= len(arr): return 0
        
        sum = total + arr[index]
        pick = self.backTrack(index+1, sum, arr, target)
        
        sum = total
        n_pick = self.backTrack(index+1, sum, arr, target)
        return pick + n_pick
        




solver = Solution()
arr = list(map(int, input("Enter the array values: ").split()))
target = int(input("Enter the target value: "))
result = solver.countSubSequencesWithSumK(arr, target)
print(result)
