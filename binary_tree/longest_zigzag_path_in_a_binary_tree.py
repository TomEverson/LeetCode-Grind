from typing import Optional
from utils import TreeNode


class Solution:
    def __init__(self):
        self.maxLen = 0  #

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.dfs(root.left, "left", 1)
        self.dfs(root.right, "right", 1)
        return self.maxLen

    def dfs(self, node: Optional[TreeNode], direction: str, length: int):
        if not node:
            return

        self.maxLen = max(self.maxLen, length)

        if direction == "right":
            self.dfs(node.left, "left", length + 1)
            self.dfs(node.right, "right", 1)
        else:
            self.dfs(node.left, "left", 1)
            self.dfs(node.right, "right", length + 1)


if __name__ == "__main__":
    root = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
    root = TreeNode.build_binary_tree(root)

    s = Solution()
    print(s.longestZigZag(root))
