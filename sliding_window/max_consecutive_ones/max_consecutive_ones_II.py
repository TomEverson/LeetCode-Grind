from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = -1
        ones = 0
        longest = 0

        for num in nums:
            if num == 1:
                ones += 1
            else:
                longest = max(longest, left + ones + 1)
                left = ones
                ones = 0

        return max(longest, left + ones + 1)


def test_solution(nums, expected):
    solution = Solution()
    result = solution.findMaxConsecutiveOnes(nums)
    print(f"Input: nums = {nums}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Basic test with a single zero in the middle
    test_solution([1, 0, 1, 1, 1], 5)

    # Test Case 2: No zeros, so the longest sequence is the entire array
    test_solution([1, 1, 1, 1], 4)

    # Test Case 3: All zeros, longest sequence with one flip is just 1
    test_solution([0, 0, 0, 0], 1)

    # Test Case 4: Multiple zeros separated by ones
    test_solution([1, 0, 1, 1, 0, 1, 1, 1], 6)

    # Test Case 5: Zero at the end of a sequence
    test_solution([1, 1, 1, 0], 4)

    # Test Case 6: Single element, either zero or one
    test_solution([1], 1)
    test_solution([0], 1)

    # Test Case 7: Long sequence with multiple zeros that can be flipped
    test_solution([1, 1, 0, 1, 1, 0, 1, 1, 1], 7)

    # Test Case 8: Alternating ones and zeros
    test_solution([1, 0, 1, 0, 1, 0, 1, 0], 3)
