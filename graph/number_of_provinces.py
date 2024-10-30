from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = [False] * len(isConnected)
        provinces = 0

        for i in range(len(isConnected)):
            if not self.visited[i]:
                provinces += 1
                self.dfs(i, isConnected)

        return provinces

    def dfs(self, i: int, isConnected: List[List[int]]):
        self.visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not self.visited[j]:
                self.dfs(j, isConnected)


if __name__ == "__main__":
    l1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    s = Solution()

    print(s.findCircleNum(l1))
