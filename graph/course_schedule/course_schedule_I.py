from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.path = set()
        self.visited = set()

        graph = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            graph[u].append(v)

        for node in graph:
            if not self.dfs(node, graph):
                return False

        return True

    def dfs(self, course: str, graph: dict[int, List[int]]) -> None:
        if course in self.path:
            return False
        if course in self.visited:
            return True

        self.path.add(course)
        for prereq in graph[course]:
            if not self.dfs(prereq, graph):
                return False

        self.path.remove(course)
        self.visited.add(course)
        return True


def test_solution(numCourses, prerequisites, expected):
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print(f"Input: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Simple case with no cycle
    test_solution(2, [[1, 0]], True)

    # Test Case 2: Simple cycle
    test_solution(2, [[1, 0], [0, 1]], False)

    # Test Case 3: No prerequisites
    test_solution(3, [], True)

    # Test Case 4: Linear dependencies
    test_solution(4, [[1, 0], [2, 1], [3, 2]], True)

    # Test Case 5: Multiple prerequisites for one course
    test_solution(3, [[1, 0], [1, 2], [0, 2]], True)

    # Test Case 6: Complex cycle
    test_solution(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]], False)

    # Test Case 7: Disconnected components
    test_solution(5, [[1, 0], [2, 3], [3, 4]], True)

    # Test Case 8: Single course with self-loop
    test_solution(1, [[0, 0]], False)

    # Test Case 9: Larger cycle
    test_solution(5, [[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]], False)

    # Test Case 10: Multiple independent paths
    test_solution(6, [[1, 0], [2, 1], [3, 2], [4, 1], [5, 4]], True)
