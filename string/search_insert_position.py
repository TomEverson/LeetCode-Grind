from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1

        if target > nums[right_ptr]:
            return len(nums)

        while left_ptr < right_ptr:
            mid_point = (left_ptr + right_ptr) // 2

            if nums[mid_point] == target:
                return mid_point

            elif nums[mid_point] > target:
                right_ptr = mid_point
            elif nums[mid_point] < target:
                left_ptr = mid_point + 1

        return left_ptr


if __name__ == "__main__":
    nums = [1, 3, 5, 7]
    target = 8

    s = Solution()
    print((0 + 1) // 2)
    print(s.searchInsert(nums, target))
