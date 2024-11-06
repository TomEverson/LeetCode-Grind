from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        max_num = sec_max_num = third_max_num = float("-inf")

        for num in nums:
            if num > max_num:
                third_max_num = sec_max_num
                sec_max_num = max_num
                max_num = num
            elif max_num > num > sec_max_num:
                third_max_num = sec_max_num
                sec_max_num = num
            elif sec_max_num > num > third_max_num:
                third_max_num = num

        return third_max_num if third_max_num != float("-inf") else max_num


def test_solution(nums, expected):
    solution = Solution()
    result = solution.thirdMax(nums)
    print(f"Input: nums = {nums}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Normal case with distinct numbers
    test_solution([3, 2, 1], 1)

    # Test Case 2: Less than three distinct numbers
    test_solution([1, 2], 2)

    # Test Case 3: With duplicates
    test_solution([2, 2, 3, 1], 1)

    # Test Case 4: All negative numbers
    test_solution([-1, -2, -3, -4], -3)

    # Test Case 5: Mixed positive and negative numbers
    test_solution([5, 2, -1, 3, 5], 0)

    # Test Case 6: Three distinct numbers
    test_solution([1, 2, 3], 1)

    # Test Case 7: Only one distinct number
    test_solution([1, 1, 1], 1)

    # Test Case 8: Three large distinct numbers
    test_solution([100, 200, 300], 100)

    # Test Case 9: Large array with duplicates
    test_solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 3)

    # Test Case 10: Very large numbers
    test_solution([2147483647, 2147483646, 2147483645], 2147483645)

    # Test Case 11: Very large numbers
    test_solution([1, 1, 2], 2)
