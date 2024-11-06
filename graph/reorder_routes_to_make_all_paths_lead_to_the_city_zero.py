from typing import List
from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        queue = deque([0])
        visited = set([0])
        changes = 0

        while queue:
            city = queue.popleft()
            for neighbor, direction in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    changes += direction
                    queue.append(neighbor)

        return changes
