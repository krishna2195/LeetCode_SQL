class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows = len(board)
        cols = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def mark_border_region(row, col):
            if not (0 <= row < rows and 0 <= col < cols) or board[row][col] != 'O':
                return
            board[row][col] = '#'
            for dx, dy in directions:
                mark_border_region(row + dx, col + dy)

        for row in range(rows):
            mark_border_region(row, 0)
            mark_border_region(row, cols - 1)

        for col in range(cols):
            mark_border_region(0, col)
            mark_border_region(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'