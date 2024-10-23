from typing import List


#! You should solve this in O(1) Space
#! No Hashset allow
#! Array is sorted

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_index = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1

        return unique_index


if __name__ == "__main__":
    l1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()

    print(s.removeDuplicates(l1))
