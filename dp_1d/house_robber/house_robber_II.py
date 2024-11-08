from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        return max(self.recursiveHelper(nums[1:]),
                   self.recursiveHelper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            maxRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = maxRob

        return rob2

    def recursiveHelper(self, nums: List[int]) -> int:
        memo = {}

        def backtrack(i: int):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            rob = nums[i] + backtrack(i + 2)

            skip = backtrack(i + 1)

            memo[i] = max(rob, skip)
            return memo[i]

        return backtrack(0)
