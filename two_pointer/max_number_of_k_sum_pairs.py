from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1
        count = 0

        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1

        return count


if __name__ == "__main__":
    s = Solution()

    print(s.maxOperations([1, 2, 3, 4], 5))
