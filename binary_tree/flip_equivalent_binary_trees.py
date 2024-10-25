from utils import TreeNode
from typing import Optional


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1, root2)

    def dfs(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        regular_check = self.dfs(root1.left, root2.left) and self.dfs(
            root1.right, root2.right)

        flipped_check = self.dfs(root1.left, root2.right) and self.dfs(
            root1.right, root2.left)

        return regular_check or flipped_check


if __name__ == "__main__":

    s = Solution()

    l1 = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
    l2 = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]
    tree = TreeNode.build_binary_tree(l1)
    tree_two = TreeNode.build_binary_tree(l2)

    result = s.flipEquiv(tree, tree_two)

    print(result)
