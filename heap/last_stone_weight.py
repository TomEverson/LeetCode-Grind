from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            res = abs(second) - abs(first)
            heapq.heappush(stones, res)

        return abs(stones[0])


if __name__ == "__main__":

    s = Solution()

    l1 = [2, 7, 4, 1, 8, 1]

    print(s.lastStoneWeight(l1))
