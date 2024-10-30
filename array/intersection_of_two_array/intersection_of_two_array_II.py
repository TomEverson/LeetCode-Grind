from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for n in nums2:
            if n in nums1:
                res.append(n)
                nums1.remove(n)

        return res
