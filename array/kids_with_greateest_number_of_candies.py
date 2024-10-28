from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_num = max(candies)

        for idx, num in enumerate(candies):
            if num + extraCandies >= max_num:
                candies[idx] = True
            else:
                candies[idx] = False

        return candies


if __name__ == "__main__":
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    s = Solution()
    print(s.kidsWithCandies(candies, extraCandies))
