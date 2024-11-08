from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         memo = {}

#         def dfs(i: int) -> int:
#             # Base cases: no cost to reach above the last step
#             if i >= len(cost):
#                 return 0

#             # Check if already computed
#             if i in memo:
#                 return memo[i]

#             # Recursive relation: min cost to reach from step `i`
#             memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
#             return memo[i]

#         # Start from either the 0th or 1st step and choose the minimum
#         return min(dfs(0), dfs(1))
