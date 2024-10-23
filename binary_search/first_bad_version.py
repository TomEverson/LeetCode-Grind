# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def __init__(self, badVersion: int):
        self.badVersion = badVersion

    def firstBadVersion(self, n: int) -> int:
        left_ptr = 0
        right_ptr = n

        while left_ptr < right_ptr:
            mid_point = (left_ptr + right_ptr) // 2
            if self.isBadVersion(mid_point):
                right_ptr = mid_point
            else:
                left_ptr = mid_point + 1

        return left_ptr

    def isBadVersion(self, n: int) -> bool:
        if n >= self.badVersion:
            return True
        else:
            return False


if __name__ == "__main__":

    solution = Solution(badVersion=4)

    res = solution.firstBadVersion(5)

    print(res)
