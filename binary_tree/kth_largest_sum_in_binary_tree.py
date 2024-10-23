from utils import TreeNode
from typing import Optional


class Solution:

    def __init__(self):
        self.res = []

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse_level(root, 0)
        self.res.sort(reverse=True)
        if len(self.res) < k:
            return -1

        return self.res[k-1]

    def traverse_level(self, root: Optional[TreeNode], level: int):
        if not root:
            return
        if len(self.res) == level:
            self.res.append(0)

        self.res[level] += root.val

        self.traverse_level(root.left, level + 1)
        self.traverse_level(root.right, level + 1)


if __name__ == "__main__":
    root = [5, 8, 9, 2, 1, 3, 7]
    k = 4

    tree = TreeNode.build_binary_tree(root)
    solution = Solution()
    print(solution.kthLargestLevelSum(tree, k))
