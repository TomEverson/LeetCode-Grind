from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1:
            if (flowerbed[0] == 0 and n == 1) or (flowerbed[0] == 1 and n == 0) or (flowerbed[0] == 0 and n == 0):
                return True
            else:
                return False

        if len(flowerbed) < 2:
            return False

        for i in range(0, len(flowerbed)):

            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i] == 0:
                    if flowerbed[i] == flowerbed[i+1]:
                        flowerbed[i] = 1
                        n -= 1
                elif i == len(flowerbed) - 1 and flowerbed[i] == 0:
                    if flowerbed[i] == flowerbed[i-1]:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i] == 0 and flowerbed[i] == flowerbed[i-1] == flowerbed[i+1]:
                        flowerbed[i] = 1
                        n -= 1

        return n < 0


if __name__ == "__main__":
    flowerbed = [0, 0, 1, 0, 0]

    n = 1

    s = Solution()
    print(s.canPlaceFlowers(flowerbed, n))
