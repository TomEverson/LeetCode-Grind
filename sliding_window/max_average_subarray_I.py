from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum -= nums[i - k]
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)

        return max_sum / k


def test_solution(nums, k, expected):
    solution = Solution()
    result = solution.findMaxAverage(nums, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Normal case with positive numbers
    test_solution([1, 12, -5, -6, 50, 3], 4, 12.75)

    # Test Case 2: All negative numbers
    test_solution([-1, -2, -3, -4], 2, -1.5)

    # Test Case 3: Mixed positive and negative numbers
    test_solution([5, -1, -2, 3, 4], 3, 2.0)

    # Test Case 4: k equals the length of the array
    test_solution([1, 2, 3, 4, 5], 5, 3.0)

    # Test Case 5: Large k value in a small array
    test_solution([10], 1, 10.0)

    # Test Case 6: Array with zero
    test_solution([0, 0, 0, 0], 2, 0.0)

    # Test Case 7: Single element negative
    test_solution([-5], 1, -5.0)

    # Test Case 8: Large positive and negative numbers
    test_solution([100, -100, 200, -200, 300], 3, 200.0)

    # Test Case 10: All elements same
    test_solution([3, 3, 3, 3], 3, 3.0)
