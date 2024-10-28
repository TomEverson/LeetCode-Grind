from utils import TreeNode
from typing import Optional, List


class Solution:

    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.dfs(root, '')
        return self.res

    def dfs(self, root: Optional[TreeNode], path: str):
        if not root:
            return

        if path:
            path += "->" + str(root.val)
        else:
            path = str(root.val)

        if not root.left and not root.right:
            self.res.append(path)
            return

        self.dfs(root.left, path)
        self.dfs(root.right, path)


if __name__ == "__main__":
    l1 = TreeNode.build_binary_tree([1, 2, 3, 4, 5])

    s = Solution()

    print(s.binaryTreePaths(l1))
