from typing import Optional
from utils import TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            root.val = self.findMin(root.right)
            root.right = self.deleteNode(root.right, root.val)

        return root

    def findMin(self, root: TreeNode) -> int:
        while root.left:
            root = root.left
        return root.val


if __name__ == "__main__":
    l1 = TreeNode.build_binary_tree(
        [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, None, 55, 65, 90, None,
            None, None, None, None, None, None, None, None, 85, 95]
    )

    s = Solution()
    l1 = s.deleteNode(l1, 3)

    l1.display()
