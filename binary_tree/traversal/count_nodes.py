from utils import TreeNode
from typing import Optional


class Solution:

    def __init__(self):
        self.count = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        self.count += 1
        self.countNodes(root.left)
        self.countNodes(root.right)

        return self.count


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6]
    l1 = TreeNode.build_binary_tree(l1)

    s = Solution()

    print(s.countNodes(l1))
