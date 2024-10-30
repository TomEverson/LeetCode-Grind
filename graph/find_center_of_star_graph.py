from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        graph = {}
        seen = set()

        for u, v in edges:
            if u not in graph:
                graph[u] = []

            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            graph[v].append(u)

        for node in graph:
            for path in graph[node]:
                if path in seen:
                    return path
                seen.add(path)


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Star graph where center is 2
    edges1 = [[1, 2], [2, 3], [4, 2]]
    print("Test 1 (Center is 2):", sol.findCenter(edges1))  # Should print 2

    # Test 2: Star graph with center at 1
    edges2 = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print("Test 2 (Center is 1):", sol.findCenter(edges2))  # Should print 1

    # Test 3: Star graph where center is 6
    edges3 = [[6, 3], [6, 4], [6, 5], [6, 1]]
    print("Test 3 (Center is 6):", sol.findCenter(edges3))  # Should print 6

    # Test 4: Star graph where center is 10 with larger values
    edges4 = [[10, 20], [30, 10], [40, 10]]
    print("Test 4 (Center is 10):", sol.findCenter(edges4))  # Should print 10

    # Test 5: Star graph with center at 8
    edges5 = [[7, 8], [8, 9], [8, 10]]
    print("Test 5 (Center is 8):", sol.findCenter(edges5))  # Should print 8
