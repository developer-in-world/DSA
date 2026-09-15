class Solution:
    def __isSafe(self,n, row, col, board):
        duprow = row
        dupcol = col
        
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
            
        row = duprow
        col = dupcol
        
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1
        
        row = duprow
        col = dupcol
        
        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1
        
        return True
    
    def __solve(self, col, board, n, ans):
        
        if col == n:
            ans.append(list(board))
            return
        
        
        for row in range(n):
            if self.__isSafe(n, row, col, board):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                self.__solve(col+1, board, n, ans)
                board[row] = board[row][:col] + "." + board[row][col+1:]
            
  
        
    def bruteForceNQueens(self, n):
        ans = []
        board = ["." * n for _ in range(n)]
        
        self.__solve(0,board, n, ans) # Optimal I will update
        return ans
    
        
        
solver = Solution()
n = int(input("Enter the n value: "))
result = solver.bruteForceNQueens(n)
print(result)        