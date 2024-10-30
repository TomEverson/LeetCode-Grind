

# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         return


# if __name__ == "__main__":
#     l1 = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
#     s = Solution()

#     print(s.minReorder(6, l1))

class Solution:
    def dfs(self, node: int, visited: set, graph: dict):
        # Process the current node (e.g., print it)
        print(node)
        visited.add(node)

        # Visit all the adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, graph)

    def traverse_dfs(self, graph: dict):
        visited = set()
        for node in graph:
            if node not in visited:
                self.dfs(node, visited, graph)


# Example usage
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

sol = Solution()
sol.traverse_dfs(graph)
