from utils import TreeNode
from typing import Optional


class Solution:

    def __init__(self):
        self.res = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.right and not root.left:
            return 0

        self.dfs(root.left, "left")
        self.dfs(root.right, "right")

        return self.res

    def dfs(self, root: TreeNode, pos: str):
        if not root:
            return

        if not root.right and not root.left and pos == "left":
            self.res += root.val

        self.dfs(root.right, "right")
        self.dfs(root.left, "left")


if __name__ == "__main__":
    root = TreeNode.build_binary_tree([1, 2])
    s = Solution()

    print(s.sumOfLeftLeaves(root))
