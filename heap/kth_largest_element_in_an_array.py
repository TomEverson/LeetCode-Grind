from typing import List
import heapq
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [num for num in nums if num > pivot]
        mid = [num for num in nums if num == pivot]
        right = [num for num in nums if num < pivot]

        length_left = len(left)
        length_right = len(right)
        length_mid = len(mid)
        if k <= length_left:
            return self.findKthLargest(left, k)
        elif k > length_left + length_mid:
            return self.findKthLargest(right, k - length_mid - length_left)
        else:
            return mid[0]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    s = Solution()
    print(s.findKthLargest(nums, k))
