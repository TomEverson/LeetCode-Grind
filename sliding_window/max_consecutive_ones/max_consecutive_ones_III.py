from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


def test_solution(nums, k, expected):
    solution = Solution()
    result = solution.longestOnes(nums, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Example from LeetCode
    test_solution([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6)

    # Test Case 2: All ones
    test_solution([1, 1, 1, 1, 1], 2, 5)

    # Test Case 3: All zeros
    test_solution([0, 0, 0, 0], 2, 2)

    # Test Case 4: k = 0 (no flips allowed)
    test_solution([1, 1, 0, 0, 1, 1], 0, 2)

    # Test Case 5: k equals number of zeros
    test_solution([0, 1, 0, 1], 2, 4)

    # Test Case 6: k greater than number of zeros
    test_solution([0, 1, 0, 1], 3, 4)

    # Test Case 7: Single element array
    test_solution([0], 1, 1)

    # Test Case 8: Alternating ones and zeros
    test_solution([1, 0, 1, 0, 1, 0, 1, 0], 2, 5)

    # Test Case 9: Multiple possible windows of same length
    test_solution([1, 1, 0, 0, 1, 1], 1, 3)

    # Test Case 10: Longer sequence with sparse ones
    test_solution([0, 0, 1, 0, 0, 0, 1, 0, 0, 1], 2, 4)

    # Test Case 11: Empty array
    test_solution([], 2, 0)

    # Test Case 12: k = 1 with multiple optimal solutions
    test_solution([1, 0, 1, 0, 1], 1, 3)
