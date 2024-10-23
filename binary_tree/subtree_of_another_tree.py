from utils import TreeNode
from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right


if __name__ == "__main__":
    root = [3, 4, 5, 1, 2]
    subRoot = [4, 1, 2]

    tree_1 = TreeNode.build_binary_tree(root)
    tree_2 = TreeNode.build_binary_tree(subRoot)

    solution = Solution()
    print(solution.isSubtree(tree_1, tree_2))
