class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        
        def isValid(board, row, col):
            for i in range(n):
                if board[i][col] == 'Q':
                    return False

            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                while 0 <= r < n and 0 <= c < n:
                    if board[r][c] == 'Q':
                        return False
                    r+=dr
                    c+=dc
            return True

        def backtrack(board, row):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                if not isValid(board, row, col):
                    continue

                board[row][col] = 'Q'
                backtrack(board, row+1)
                board[row][col] = '.'
        backtrack(board, 0)
        return res        



        