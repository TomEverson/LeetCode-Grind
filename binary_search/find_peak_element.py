from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return 0

        if l == 0 and nums[l] > nums[l+1]:
            return l

        if r == len(nums) - 1 and nums[r] > nums[r-1]:
            return r

        while l < r:
            mid = (l + r) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid-1] > nums[mid]:
                r = mid
            else:
                l = mid + 1

        return


if __name__ == "__main__":
    nums = [1, 2, 3, 1]

    s = Solution()
    print(s.findPeakElement(nums))
