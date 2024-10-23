from typing import List


#! You should solve this in O(1) Space
#! No Hashset allow


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


if __name__ == "__main__":
    l1 = [3, 2, 2, 3]
    val = 3
    s = Solution()

    print(s.removeElement(l1, val))
