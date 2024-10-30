from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.cycle = set()
        self.visited = set()
        self.res = []
        self.graph = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            self.graph[v].append(u)

        for course in range(numCourses):
            if self.dfs(course) == False:
                return []

        self.res.reverse()

        return self.res

    def dfs(self, course):
        if course in self.cycle:
            return False
        if course in self.visited:
            return True

        self.cycle.add(course)
        for pre in self.graph[course]:
            if self.dfs(pre) == False:
                return False

        self.cycle.remove(course)
        self.visited.add(course)
        self.res.append(course)
        return True


def test_solution(numCourses, prerequisites, expected):
    solution = Solution()
    result = solution.findOrder(numCourses, prerequisites)
    print(f"Input: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":

    test_solution(4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3])

    # Test Case 1: Simple case with no prerequisites
    test_solution(2, [], [0, 1])

    # Test Case 2: Simple linear dependency
    test_solution(2, [[1, 0]], [0, 1])

    # Test Case 3: Simple cycle (no valid order)
    test_solution(2, [[1, 0], [0, 1]], None)

    # Test Case 4: No prerequisites with multiple courses
    test_solution(3, [], [0, 1, 2])

    # Test Case 5: Multiple valid topological orders
    test_solution(4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3])

    # Test Case 6: Complex cycle
    test_solution(4, [[1, 0], [2, 1], [3, 2], [1, 3]], None)

    # Test Case 7: Disconnected components
    test_solution(5, [[1, 0], [2, 3], [3, 4]], [0, 1, 4, 3, 2])

    # Test Case 8: Single course with self-loop
    test_solution(1, [[0, 0]], None)

    # Test Case 9: Larger acyclic graph
    test_solution(5, [[1, 0], [2, 1], [3, 2], [4, 3]], [0, 1, 2, 3, 4])

    # Test Case 10: Multiple independent paths
    test_solution(6, [[1, 0], [2, 1], [4, 3], [5, 4]], [0, 1, 2, 3, 4, 5])
