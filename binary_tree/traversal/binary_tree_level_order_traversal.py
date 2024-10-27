from utils import TreeNode
from typing import Optional, List


class Solution:

    def __init__(self):
        self.res = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse_level(root, 0)
        return self.res

    def traverse_level(self, root: Optional[TreeNode], level: int):
        if not root:
            return

        if len(self.res) == level:
            self.res.append([])

        self.res[level].append(root.val)

        self.traverse_level(root.left, level + 1)
        self.traverse_level(root.right, level + 1)


if __name__ == "__main__":
    l1 = [3, 9, 20, None, None, 15, 7]
    tree = TreeNode.build_binary_tree(l1)

    solution = Solution()

    print(solution.levelOrder(tree))
