from utils import TreeNode
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":

    solution = Solution()

    tree = TreeNode.build_binary_tree([4, 2, 7, 1, 3, 6, 9])

    new_tree = solution.invertTree(tree)

    new_tree.display()
