class Solution:
    def __solve(self, digits, index, subset, result):
        char_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
                    "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        if index >= len(digits):
            result.append("".join(subset))
            return
        
        for ch in char_map[digits[index]]:
            subset.append(ch)
            self.__solve(digits, index+1, subset, result)
            subset.pop()
            
    def LetterCombosOfPhoneNumber(self, digits):
        result = []
        self.__solve(digits, 0, [], result)
        return result
    

solver = Solution()
digits = input("Enter the numbers (_,_,_,_) only 4 max: ")
result = solver.LetterCombosOfPhoneNumber(digits)
print(result)
        