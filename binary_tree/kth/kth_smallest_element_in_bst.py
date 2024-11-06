from utils import TreeNode
from typing import Optional


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        self.dfs(root)
        return self.res[k-1]

    def dfs(self, root: TreeNode):
        if not root:
            return

        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)


if __name__ == "__main__":
    l1 = [4, 2, 6, 1, 3, 5, 7]
    k = 2
    tree = TreeNode.build_binary_tree(l1)

    s = Solution()
    print(s.kthSmallest(tree, k))
