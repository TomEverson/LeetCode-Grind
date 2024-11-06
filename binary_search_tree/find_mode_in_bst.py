from utils import TreeNode
from typing import Optional, List


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.counts = {}
        modes = []

        self.dfs(root)
        max_count = max(self.counts.values(), default=0)
        modes = [key for key, value in self.counts.items() if value ==
                 max_count]

        return modes

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return

        self.dfs(root.left)
        self.counts[root.val] = self.counts.get(root.val, 0) + 1
        self.dfs(root.right)
