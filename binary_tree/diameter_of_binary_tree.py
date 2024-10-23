from utils import TreeNode
from typing import Optional


class Solution:

    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.res = max(self.res, left + right)

        return 1 + max(left, right)
