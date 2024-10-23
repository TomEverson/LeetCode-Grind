from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        hashmap = {}
        idx = 0
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for color in range(3):
            freq = hashmap.get(color, 0)
            nums[idx: idx + freq] = [color] * freq
            idx += freq


if __name__ == "__main__":
    l1 = [2, 0, 2, 1, 1, 0]

    solution = Solution()

    res = solution.sortColors(l1)

    print(res)
