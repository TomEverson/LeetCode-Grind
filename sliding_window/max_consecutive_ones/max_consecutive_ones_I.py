from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        max_count = 0
        count = 0

        while l < len(nums):
            if nums[l] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

            l += 1

        return max_count


def test_solution(nums, expected):
    solution = Solution()
    result = solution.findMaxConsecutiveOnes(nums)
    print(f"Input: nums = {nums}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Normal case with mixed zeros and ones
    test_solution([1, 1, 0, 1, 1, 1], 3)

    # Test Case 2: All ones
    test_solution([1, 1, 1, 1], 4)

    # Test Case 3: All zeros
    test_solution([0, 0, 0, 0], 0)

    # Test Case 4: Single element (one)
    test_solution([1], 1)

    # Test Case 5: Single element (zero)
    test_solution([0], 0)

    # Test Case 6: Longest sequence at the start
    test_solution([1, 1, 1, 0, 0, 0], 3)

    # Test Case 7: Longest sequence at the end
    test_solution([0, 0, 1, 1, 1], 3)

    # Test Case 8: Multiple sequences of ones
    test_solution([1, 0, 1, 1, 0, 1], 2)

    # Test Case 9: Alternating ones and zeros
    test_solution([1, 0, 1, 0, 1, 0], 1)
