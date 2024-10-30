from typing import List
from collections import deque
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()
        islands = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == "1" and (r, c) not in self.visited:
                    self.bfs(r, c, grid)
                    islands += 1

        return islands

    def bfs(self, r: int, c: int, grid: List[List[str]]):
        q = deque()
        self.visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and grid[nr][nc] == '1' and (nr, nc) not in self.visited:
                    q.append((nr, nc))
                    self.visited.add((nr, nc))


if __name__ == "__main__":
    sol = Solution()

    # # Test 1: Single large island covering most of the grid
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print("Test 1 (One large island):",
          sol.numIslands(grid1))  # Expected output: 1

    # Test 2: Multiple islands scattered across the grid
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print("Test 2 (Three separate islands):",
          sol.numIslands(grid2))  # Expected output: 3

    # # Test 3: Grid with no land (only water)
    grid3 = [
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"]
    ]
    print("Test 3 (No islands):", sol.numIslands(grid3))  # Expected output: 0

    # # Test 4: Diagonally adjacent '1's (not connected horizontally or vertically)
    grid4 = [
        ["1", "0", "0", "1"],
        ["0", "1", "1", "0"],
        ["1", "0", "0", "1"]
    ]
    print("Test 4 (Six diagonal islands):",
          sol.numIslands(grid4))  # Expected output: 6

    # # Test 5: All land (one large island)
    grid5 = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    print("Test 5 (One large island):",
          sol.numIslands(grid5))  # Expected output: 1

    # # Test 6: Small grid with a single '1'
    grid6 = [["1"]]
    print("Test 6 (One small island):",
          sol.numIslands(grid6))  # Expected output: 1

    # # Test 7: Single column with alternating land and water
    grid7 = [
        ["1"],
        ["0"],
        ["1"],
        ["0"],
        ["1"]
    ]
    print("Test 7 (Three vertical islands):",
          sol.numIslands(grid7))  # Expected output: 3
