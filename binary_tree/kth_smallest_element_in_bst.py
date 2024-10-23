from utils import TreeNode
from typing import Optional


class Solution:
    def __init__(self):
        self.count = 0
        self.result = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root, k)
        return self.result

    def inorder(self, root: Optional[TreeNode], k: int):
        if not root:
            return

        self.inorder(root.left, k)

        self.count += 1
        if self.count == k:
            self.result = root.val
            return

        self.inorder(root.right, k)


if __name__ == "__main__":
    l1 = [4, 2, 6, 1, 3, 5, 7]
    k = 2
    tree = TreeNode.build_binary_tree(l1)

    s = Solution()
    print(s.kthSmallest(tree, k))
