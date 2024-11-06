from typing import List
import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while q or maxHeap:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time


if __name__ == "__main__":

    s = Solution()

    tasks = ["A", "A", "A", "B", "C"]
    n = 3

    print(s.findKthLargest(tasks, n))
