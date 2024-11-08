from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def backtrack(i):

            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            rob = nums[i] + backtrack(i + 2)

            skip = backtrack(i + 1)

            memo[i] = max(rob, skip)
            return memo[i]

        return backtrack(0)


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         rob1, rob2 = 0, 0

#         for num in nums:
#             temp = max(num + rob1, rob2)
#             rob1 = rob2
#             rob2 = temp
#         return rob2
