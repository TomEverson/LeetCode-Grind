from typing import Optional
from utils import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = [root.val]
        self.dfs(root)

        return self.res[0]

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0

        leftMax = self.dfs(root.left)
        rightMax = self.dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        self.res[0] = max(self.res[0], root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)
