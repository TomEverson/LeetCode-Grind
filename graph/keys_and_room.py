from typing import List, Set


class Solution:

    def __init__(self):
        self.visited = set()

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.dfs(0, rooms)
        return len(self.visited) == len(rooms)

    def dfs(self, room: int, rooms: List[List[int]]):
        self.visited.add(room)
        for i in rooms[room]:
            if i not in self.visited:
                self.dfs(i, rooms)


if __name__ == "__main__":
    l1 = [[1], [2], [3], []]

    s = Solution()
    print(s.canVisitAllRooms(l1))
