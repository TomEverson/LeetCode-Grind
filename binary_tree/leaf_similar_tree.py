from utils import TreeNode
from typing import Optional


class Solution:

    def __init__(self):
        self.set_one = []
        self.set_two = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.dfs(root1, 1)
        self.dfs(root2, 2)
        return self.set_one == self.set_two

    def dfs(self, root: Optional[TreeNode], set: int):
        if not root:
            return

        if not root.left and not root.right:
            self.set_one.append(root.val) if set == 1 else None
            self.set_two.append(root.val) if set == 2 else None

        self.dfs(root.left, set)
        self.dfs(root.right, set)


if __name__ == "__main__":
    root1 = [1, 2, 3]
    root2 = [1, 3, 2]

    l1 = TreeNode.build_binary_tree(root1)
    l2 = TreeNode.build_binary_tree(root2)

    s = Solution()

    print(s.leafSimilar(l1, l2))
