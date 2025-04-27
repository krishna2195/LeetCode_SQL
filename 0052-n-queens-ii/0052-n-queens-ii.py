class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.'] * n for _ in range(n)]
        count = [0]

        # \U0001f6e1️ Check if it's safe to place a queen
        def is_safe(row, col):
            for c in range(col):
                if board[row][c] == 'Q':
                    return False
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            r, c = row, col
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1
            return True

        # \U0001f501 Backtracking helper
        def backtrack(col):
            if col == n:
                count[0] += 1  # \U0001f3af Valid configuration found
                return
            for row in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'   # \U0001f451 Place queen
                    backtrack(col + 1)
                    board[row][col] = '.'   # ↩️ Backtrack

        backtrack(0)
        return count[0]