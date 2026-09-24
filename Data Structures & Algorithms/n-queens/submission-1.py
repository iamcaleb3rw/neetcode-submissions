class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        usedCols = set()
        mainDiag = set()
        reverseDiag = set()
        def backtrack(board, row):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                if (col in usedCols) or (row+col in reverseDiag) or (row-col in mainDiag):
                    continue
 
                board[row][col] = 'Q'
                usedCols.add(col)
                mainDiag.add(row-col)
                reverseDiag.add(row+col)

                backtrack(board, row+1)
                
                board[row][col] = '.'
                usedCols.remove(col)
                mainDiag.remove(row-col)
                reverseDiag.remove(row+col)
        backtrack(board, 0)
        return res        



        