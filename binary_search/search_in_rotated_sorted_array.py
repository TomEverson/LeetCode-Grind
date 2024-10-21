from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_ptr, right_ptr = 0, len(nums) - 1

        while left_ptr <= right_ptr:
            midpoint = (left_ptr + right_ptr) // 2

            if nums[midpoint] == target:
                return midpoint

            if nums[left_ptr] <= nums[midpoint]:
                if target > nums[midpoint] or target < nums[left_ptr]:
                    left_ptr = midpoint + 1
                else:
                    right_ptr = midpoint - 1
            else:
                if target < nums[midpoint] or target > nums[right_ptr]:
                    right_ptr = midpoint - 1
                else:
                    left_ptr = midpoint + 1

        return -1


solution = Solution()

print(solution.search([4, 5, 6, 7, 0, 1, 2], 10))  # ! 4
