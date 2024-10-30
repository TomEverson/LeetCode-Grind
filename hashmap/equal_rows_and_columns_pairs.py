from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        for i in range(n):
            row = ','.join(map(str, grid[i]))
            for j in range(n):
                col = ','.join(str(grid[k][j]) for k in range(n))
                if col == row:
                    res += 1
        return res


if __name__ == "__main__":
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

    s = Solution()
    print(s.equalPairs(grid))
