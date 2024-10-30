from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.visited = set()

        # Fix 1: Swap ROWS and COLS
        self.ROWS = len(board)
        self.COLS = len(board[0])

        # Start from border O's
        # First and last row
        for col in range(self.COLS):
            if board[0][col] == "O":
                self.dfs(0, col, board)
            if board[self.ROWS-1][col] == "O":
                self.dfs(self.ROWS-1, col, board)

        # First and last column
        for row in range(self.ROWS):
            if board[row][0] == "O":
                self.dfs(row, 0, board)
            if board[row][self.COLS-1] == "O":
                self.dfs(row, self.COLS-1, board)

        # Convert remaining O's to X's and visited ones back to O's
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == "O" and (row, col) not in self.visited:
                    board[row][col] = "X"
                elif (row, col) in self.visited:
                    board[row][col] = "O"

    def dfs(self, row: int, col: int, board: List[List[str]]):
        stack = [(row, col)]

        while stack:
            row, col = stack.pop()
            if (row, col) in self.visited or board[row][col] == "X":
                continue

            self.visited.add((row, col))

            # Fix 2: Correct boundary conditions
            if row + 1 < self.ROWS:
                if board[row + 1][col] == "O":
                    stack.append((row + 1, col))
            if row - 1 >= 0:
                if board[row - 1][col] == "O":
                    stack.append((row - 1, col))
            if col + 1 < self.COLS:
                if board[row][col + 1] == "O":
                    stack.append((row, col + 1))
            if col - 1 >= 0:
                if board[row][col - 1] == "O":
                    stack.append((row, col - 1))


if __name__ == "__main__":
    sol = Solution()  # Assume your class is named Solution

    # Test case 1: All cells are 'X'
    board1 = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

    print(sol.solve(board1))
