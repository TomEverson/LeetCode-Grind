from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True


if __name__ == "__main__":
    # Instantiate the solution class
    solution = Solution()

    # Test Case 1: Non-overlapping intervals
    intervals1 = [Interval(1, 3), Interval(5, 8), Interval(9, 12)]
    print(solution.canAttendMeetings(intervals1))  # Expected Output: True

    # Test Case 2: Overlapping intervals
    intervals2 = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    print(solution.canAttendMeetings(intervals2))  # Expected Output: False

    # Test Case 3: Consecutive but non-overlapping intervals
    intervals3 = [Interval(1, 5), Interval(5, 10), Interval(10, 15)]
    print(solution.canAttendMeetings(intervals3))  # Expected Output: True
