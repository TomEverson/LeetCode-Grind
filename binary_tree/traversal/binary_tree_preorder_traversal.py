from utils import TreeNode
from typing import Optional, List


class Solution:

    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        self.res.append(root.val)

        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.res


if __name__ == "__main__":

    s = Solution()

    l1 = TreeNode.build_binary_tree(
        [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])

    print(s.preorderTraversal(l1))
