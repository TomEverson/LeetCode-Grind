from typing import List, Optional
from utils import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional['TreeNode']:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


if __name__ == '__main__':
    l1 = [-10, -3, 0, 5, 9]

    s = Solution()
    l1 = s.sortedArrayToBST(l1)
    l1.display()
