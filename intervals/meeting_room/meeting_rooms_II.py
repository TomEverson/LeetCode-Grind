from typing import List
import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)


if __name__ == "__main__":
    # Instantiate the solution class
    solution = Solution()

    # Test Case 1: Non-overlapping intervals
    intervals1 = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    print(solution.minMeetingRooms(intervals1))  # Expected Output: True
