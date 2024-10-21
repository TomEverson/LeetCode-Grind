from typing import List

# [3,4,5,1,2]
# [4,5,6,7,0,1,2]
# [12,13,8,10]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_ptr, right_ptr = 0, len(nums) - 1

        while left_ptr < right_ptr:
            mid_point = (left_ptr + right_ptr) // 2
            if nums[left_ptr] > nums[right_ptr]:
                if nums[mid_point] < nums[right_ptr]:

                    right_ptr = mid_point

                else:
                    left_ptr = mid_point + 1
            elif nums[right_ptr] > nums[left_ptr]:
                right_ptr = mid_point - 1

        return nums[left_ptr]


solution = Solution()

print(solution.findMin([3, 1, 2]))
