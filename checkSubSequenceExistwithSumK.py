class Solution:
    def checkSubSequenceExistWithSumK(self, arr, k):
        print(self.TrueorFalseOnly(0, k, 0, arr))
        # if the interviewer only asks for True or False we just remove the subset and some changes to the existing below code and it will work
        
        
    def backtrack(self, index, target, total, arr, subset, result):
        if total == target:
            result.append(subset.copy())
            return True
        if total > target:
            return False
        if index >= len(arr):
            return False # this code can be used to check whether it exist or not or also find the any one sequence where the sum k exist
        
        subset.append(arr[index])
        total += arr[index]
        pick = self.backtrack(index+1, target, total, arr, subset, result)
        if pick == True: return True
        
        e = subset.pop()
        total -= e
        not_pick = self.backtrack(index+1, target, total, arr, subset, result)
        return not_pick
    
    def TrueorFalseOnly(self, index, target, total, arr):
        if total == target: return True
        elif total > target: return False
        elif index >= len(arr): return False
        
        sum = total + arr[index]
        pick = self.TrueorFalseOnly(index+1, target, sum, arr)
        if pick == True: return True
        
        sum = total
        not_pick = self.TrueorFalseOnly(index+1, target, sum, arr)
        return not_pick
        
        
        
        
        





solver = Solution()
arr = list(map(int, input("Enter the array values: ").split()))
target = int(input("Enter the target value: "))
solver.checkSubSequenceExistWithSumK(arr, target)

