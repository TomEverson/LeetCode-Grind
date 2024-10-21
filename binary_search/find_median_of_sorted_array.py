from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        left_ptr, right_ptr = 0, 0
        while left_ptr < len(nums1) and right_ptr < len(nums2):
            if nums1[left_ptr] < nums2[right_ptr]:
                merged.append(nums1[left_ptr])
                left_ptr += 1
            else:
                merged.append(nums2[right_ptr])
                right_ptr += 1

        merged.extend(nums1[left_ptr:])
        merged.extend(nums2[right_ptr:])

        print(merged)

        if (len(merged) % 2) != 0:
            return merged[(len(merged) - 1) // 2]
        else:
            midpoint_one = (len(merged) - 1) // 2
            midpoint_two = ((len(merged) - 1) // 2) + 1
            return (merged[midpoint_one] + merged[midpoint_two]) / 2


solution = Solution()

print(solution.findMedianSortedArrays([1, 2], [3, 4]))
