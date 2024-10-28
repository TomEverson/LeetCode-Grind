from typing import List


class Solution:
    def increasingTriplet(self, nums):
        min1 = float('inf')
        min2 = float('inf')
        for n in nums:
            if n <= min1:
                min1 = n
            elif n <= min2:
                min2 = n
            else:
                return True
        return False


if __name__ == "__main__":
    # nums = [1, 2, 3, 4, 5]
    nums = [20, 100, 10, 12, 5, 13]

    s = Solution()
    print(s.increasingTriplet(nums))
