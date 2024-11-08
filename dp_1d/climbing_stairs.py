
# ? Bottom Up DP
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         prev, curr = 1, 1

#         for _ in range(n - 1):
#             prev, curr = curr, prev + curr

#         return curr

# ? Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(steps: int) -> int:
            # Base cases
            if steps <= 1:
                return 1

            # Check memo to avoid recomputation
            if steps in memo:
                return memo[steps]

            # Recursive relation with memoization
            memo[steps] = dfs(steps - 1) + dfs(steps - 2)
            return memo[steps]

        return dfs(n)
