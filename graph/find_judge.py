from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        graph = {i: [] for i in range(1, n + 1)}
        trust_counts = [0] * (n + 1)

        for u, v in trust:
            graph[u].append(v)
            trust_counts[v] += 1

        for person in range(1, n + 1):

            if not graph[person] and trust_counts[person] == n - 1:
                return person

        return -1


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Simple case where the judge exists
    n1 = 3
    trust1 = [[1, 3], [2, 3]]
    print("Test 1 (Judge is 3):", sol.findJudge(n1, trust1))  # Should print 3

    # Test 2: No judge (everyone trusts each other)
    n2 = 3
    trust2 = [[1, 3], [2, 3], [3, 1]]
    print("Test 2 (No judge):", sol.findJudge(n2, trust2))  # Should print -1

    # Test 3: Single person, automatically the judge
    n3 = 1
    trust3 = []
    print("Test 3 (Judge is 1):", sol.findJudge(n3, trust3))  # Should print 1

    # Test 4: Judge is the only one trusted by everyone
    n4 = 4
    trust4 = [[1, 3], [2, 3], [4, 3]]
    print("Test 4 (Judge is 3):", sol.findJudge(n4, trust4))  # Should print 3

    # Test 5: No judge due to multiple trusted people
    n5 = 4
    trust5 = [[1, 3], [2, 3], [4, 3], [1, 4]]
    print("Test 5 (No judge):", sol.findJudge(n5, trust5))  # Should print -1
