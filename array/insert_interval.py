from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left_ptr = 0
        right_ptr = len(intervals) - 1

        while left_ptr < right_ptr:
            mid_point = (left_ptr + right_ptr) // 2
            num_list = intervals[mid_point]

        return


if __name__ == "__main__":
    intervals = [[1, 3], [6, 9]],
    newInterval = [2, 5]

    solution = Solution()

    res = solution.insert(intervals, newInterval)

    print(res)
