from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()
        self.res = []

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1 and (r, c) not in self.visited:
                    self.bfs(r, c, grid)

        return max(self.res) if self.res else 0

    def bfs(self, r: int, c: int, grid: List[List[str]]):
        q = deque()
        self.visited.add((r, c))
        q.append((r, c))
        count = 1

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for d_row, d_col in directions:
                new_row, new_col = row + d_row, col + d_col
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and grid[new_row][new_col] == 1 and (new_row, new_col) not in self.visited:
                    q.append((new_row, new_col))
                    self.visited.add((new_row, new_col))
                    count += 1

        self.res.append(count)


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Provided Example
    grid1 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    print("Test Case 1 (Expected Output: 6):", sol.maxAreaOfIsland(grid1))

    # Test Case 2: No islands
    grid2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print("Test Case 2 (Expected Output: 0):", sol.maxAreaOfIsland(grid2))

    # Test Case 3: Single island
    grid3 = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 0, 0]
    ]
    print("Test Case 3 (Expected Output: 4):", sol.maxAreaOfIsland(grid3))

    # Test Case 4: Multiple separate islands
    grid4 = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]
    print("Test Case 4 (Expected Output: 5):", sol.maxAreaOfIsland(grid4))

    # Test Case 5: Large island
    grid5 = [
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    print("Test Case 5 (Expected Output: 6):", sol.maxAreaOfIsland(grid5))

    # Test Case 6: Irregular shapes
    grid6 = [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]
    ]
    print("Test Case 6 (Expected Output: 5):", sol.maxAreaOfIsland(grid6))
