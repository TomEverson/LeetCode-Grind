from utils import TreeNode
from typing import Optional, List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        self.dfs(root, [], targetSum)

        return self.res

    def dfs(self, node: TreeNode, path: List[int], targetSum: int):
        if not node:
            return

        path.append(node.val)
        targetSum -= node.val

        if not node.left and not node.right and targetSum == 0:
            print(targetSum)
            self.res.append(path[:])
        else:
            self.dfs(node.left, path, targetSum)
            self.dfs(node.right, path, targetSum)
        path.pop()


if __name__ == "__main__":
    root = TreeNode.build_binary_tree(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    targetSum = 22

    s = Solution()

    print(s.pathSum(root, targetSum))
