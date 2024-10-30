from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        diff_1 = nums1.difference(nums2)
        diff_2 = nums2.difference(nums1)
        return [list(diff_1), list(diff_2)]


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]

    s = Solution()
    print(s.findDifference(nums1, nums2))
