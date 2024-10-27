from utils import TreeNode
from typing import Optional, List


class Solution:

    def __init__(self):
        self.res = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)

        self.res.append(root.val)

        return self.res


if __name__ == "__main__":
    s = Solution()
    l1 = TreeNode.build_binary_tree(
        [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])

    s.postorderTraversal(l1)

    print(s.res)
