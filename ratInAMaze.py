class Solution:
    def ratMaze(self, matrix):
        n = len(matrix)
        ans = []
        visted_path_array = [[0 for _ in range(n)] for _ in range(n)]
        
        if not matrix:
            return []
        
        if matrix[0][0] == 1:
            visted_path_array[0][0] = 1
            self.__findPath(0, 0, matrix, n, ans, "", visted_path_array)
        
        return ans
    
    def __findPath(self, i, j, matrix, n, ans, move, visitedPathArr):
        
        if i == n-1 and j == n-1:
            ans.append(move)
            return
        
        # down
        if i+1 < n and not visitedPathArr[i+1][j] and matrix[i+1][j] == 1:
            visitedPathArr[i+1][j] = 1
            self.__findPath(i+1, j, matrix, n, ans, move+"D", visitedPathArr)
            visitedPathArr[i+1][j] = 0
        
        # left
        if j-1 >= 0 and not visitedPathArr[i][j-1] and matrix[i][j-1] == 1:
            visitedPathArr[i][j-1] = 1
            self.__findPath(i, j-1, matrix, n, ans, move+"L", visitedPathArr)
            visitedPathArr[i][j-1] = 0
        
        # right
        if j+1 < n and not visitedPathArr[i][j+1] and matrix[i][j+1] == 1:
            visitedPathArr[i][j+1] = 1
            self.__findPath(i, j+1, matrix, n, ans, move+"R", visitedPathArr)
            visitedPathArr[i][j+1] = 0
        
        # up
        if i-1 >= 0 and not visitedPathArr[i-1][j] and matrix[i-1][j] == 1:
            visitedPathArr[i-1][j] = 1
            self.__findPath(i-1, j, matrix, n, ans, move+"U", visitedPathArr)
            visitedPathArr[i-1][j] = 0
        

n = int(input("Enter the n\' to create a (square matrix) : "))
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

solver = Solution()
result = solver.ratMaze(matrix)
print(result)      