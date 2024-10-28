from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        n_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)

        return n_sum - actual_sum


if __name__ == "__main__":
    l1 = [3, 0, 1]

    s = Solution()
    print(s.missingNumber(l1))
