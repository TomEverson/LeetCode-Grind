from utils import TreeNode
from typing import Optional, List


class Solution:

    def __init__(self):
        self.res = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dfs(root, 0)
        return self.res

    def dfs(self, root: Optional[TreeNode], level: int):
        if not root:
            return

        if len(self.res) == level:
            self.res.append([])

        self.res[level].append(root.val)

        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)


if __name__ == "__main__":
    l1 = [3, 9, 20, None, None, 15, 7]
    tree = TreeNode.build_binary_tree(l1)

    solution = Solution()

    print(solution.levelOrder(tree))
