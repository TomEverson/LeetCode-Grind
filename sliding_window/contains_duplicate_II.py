from typing import List
from collections import deque


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False


if __name__ == "__main__":
    nums = [1, 2, 1, 1]
    k = 3

    s = Solution()
    print(s.containsNearbyDuplicate(nums, k))
