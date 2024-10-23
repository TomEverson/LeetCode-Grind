from utils import TreeNode
from typing import Optional, List


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return [True, 0]

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return [balanced, 1 + max(left[1], right[1])]


if __name__ == "__main__":
    solution = Solution()
    tree = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])

    print(solution.isBalanced(tree))

    tree.display()
