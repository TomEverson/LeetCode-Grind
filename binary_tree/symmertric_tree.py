from utils import TreeNode
from typing import Optional


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

        if not left and not right:
            return True

        if not left or not right:
            return False

        val_equal = left.val == right.val

        left_mirror = self.isMirror(left.left, right.right)
        right_mirror = self.isMirror(left.right, right.left)

        return val_equal and left_mirror and right_mirror


if __name__ == "__main__":
    s = Solution()

    l1 = TreeNode.build_binary_tree([1, 2, 2, 3, 4, 4, 3])
    l1 = s.isSymmetric(l1)

    # l1.display()

    print(l1)
