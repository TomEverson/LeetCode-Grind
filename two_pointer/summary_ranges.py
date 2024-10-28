from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        res = []

        if len(nums) < 2:
            return [str(num) for num in nums]

        left_ptr = 0
        right_ptr = 1

        while left_ptr < len(nums):
            start = None
            end = None
            while right_ptr < len(nums) and nums[right_ptr - 1] == nums[right_ptr] - 1:
                end = nums[right_ptr]
                right_ptr += 1

            start = nums[left_ptr]

            if start is not None and end is not None:
                res.append(f'{start}->{end}')
            else:
                res.append(str(start))

            left_ptr = right_ptr

            right_ptr += 1

        return res


if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 7]
    # nums = [0, 1]

    s = Solution()
    print(s.summaryRanges(nums))
