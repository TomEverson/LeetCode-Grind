from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        zeros = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == len(nums) else ans


def test_solution(nums, expected):
    solution = Solution()
    result = solution.longestSubarray(nums)
    print(f"Input: nums = {nums}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Basic case with one zero
    test_solution([1, 1, 0, 1, 1, 1], 5)

    # Test Case 2: No zeros, longest subarray after deleting one element
    test_solution([1, 1, 1, 1], 3)

    # Test Case 3: All zeros, no consecutive 1s possible
    test_solution([0, 0, 0, 0], 0)

    # Test Case 4: Edge case with only one element
    test_solution([1], 0)
    test_solution([0], 0)

    # Test Case 5: Alternating ones and zeros
    test_solution([1, 0, 1, 0, 1, 0, 1], 2)

    # Test Case 6: Multiple consecutive 1's separated by single 0's
    test_solution([1, 1, 0, 1, 1, 0, 1, 1], 4)

    # Test Case 7: Long sequence of ones, one zero in the middle
    test_solution([1, 1, 1, 1, 0, 1, 1, 1, 1], 8)

    # Test Case 8: Only one 0 at the beginning
    test_solution([0, 1, 1, 1, 1], 4)

    # Test Case 9: Only one 0 at the end
    test_solution([1, 1, 1, 1, 0], 4)
