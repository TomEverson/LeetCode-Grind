from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        for g in range(1, len(gain)):
            gain[g] = gain[g-1] + gain[g]

        return max([0] + gain)


if __name__ == "__main__":
    l1 = [-5, 1, 5, 0, -7]

    s = Solution()

    print(s.largestAltitude(l1))
