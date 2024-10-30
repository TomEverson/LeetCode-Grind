from ..utils import TreeNode
from typing import Optional, List


class Solution:

    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.res

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return []

        self.dfs(root.left)

        self.res.append(root.val)

        self.dfs(root.right)


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
    l1 = TreeNode.build_binary_tree(l1)

    s = Solution()
    print(s.inorderTraversal(l1))
