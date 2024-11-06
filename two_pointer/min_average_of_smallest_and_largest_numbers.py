from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        res = []

        nums.sort()
        l = 0
        r = len(nums) - 1

        while l < r:
            average = (nums[l] + nums[r]) / 2
            res.append(average)

            l += 1
            r -= 1

        return min(res)


if __name__ == "__main__":

    s = Solution()
    print(s.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))
