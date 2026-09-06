class Solution:
    def __backTrack(self, index, flag, numbers, result):
        if index >= len(numbers):
            result.append("".join(numbers))
            return
        numbers[index] = "0"
        self.__backTrack(index+1, True, numbers, result)
        
        if flag == True:
            numbers[index] = "1"
            self.__backTrack(index+1, False, numbers, result)
            numbers[index] = "0"
        
    def WithoutConsecutiveOnes(self, n):
        numbers = ["0"]*n
        result = []
        self.__backTrack(0, True, numbers, result)
        return result
    

n = int(input("Enter the n number: "))
solver = Solution()
result = solver.WithoutConsecutiveOnes(n)
print(result)
        


