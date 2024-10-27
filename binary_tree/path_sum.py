from typing import Optional, List
from utils import TreeNode


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


if __name__ == "__main__":
    l1 = TreeNode.build_binary_tree(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])

    s = Solution()
    l2 = s.hasPathSum(l1, 22)

    print(l2)
