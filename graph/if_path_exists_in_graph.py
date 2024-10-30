from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return False


if __name__ == "__main__":
    sol = Solution()

    # Test 1: No path exists
    n1 = 6
    edges1 = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    print("Test 1 (No path):",
          sol.validPath(n1, edges1, 0, 5))  # Should print False

    # Test 2: Path exists
    n2 = 6
    edges2 = [[0, 1], [0, 2], [2, 3], [3, 5], [5, 4], [4, 3]]
    print("Test 2 (Path exists):",
          sol.validPath(n2, edges2, 0, 5))  # Should print True

    # Test 3: Cycle exists
    n3 = 3
    edges3 = [[0, 1], [1, 2], [2, 0]]
    print("Test 3 (Cycle):",
          sol.validPath(n3, edges3, 0, 2))  # Should print True
