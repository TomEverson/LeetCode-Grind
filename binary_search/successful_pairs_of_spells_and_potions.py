from typing import List


from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        for spell in spells:
            l, r = 0, len(potions)
            count = 0
            while l < r:
                mid = (l + r) // 2
                if potions[mid] * spell >= success:
                    r = mid
                else:
                    l = mid + 1
                    count = l
            res.append(len(potions) - count)

        return res


if __name__ == "__main__":
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7

    s = Solution()

    print(s.successfulPairs(spells, potions, success))
