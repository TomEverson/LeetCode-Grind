from typing import List
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            distance = math.sqrt((x ** 2) + (y ** 2))
            minHeap.append((distance, x, y))

        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res


if __name__ == '__main__':
    l1 = [[1, 3], [-2, 2]]
    k = 1

    s = Solution()
    print(s.kClosest(l1, k))
