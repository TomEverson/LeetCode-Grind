from utils import TreeNode
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode], min_val=float("-inf"), max_val=float("+inf")) -> bool:
        if not root:
            return True

        if not (min_val < root.val < max_val):
            return False

        left = self.dfs(root.left, min_val, root.val)

        right = self.dfs(root.right, root.val, max_val)

        return left and right


if __name__ == "__main__":
    l1 = [2, 1, 3]
    tree_1 = TreeNode.build_binary_tree(l1)

    s = Solution()

    print(s.isValidBST(tree_1))
