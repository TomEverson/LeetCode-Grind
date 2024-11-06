from utils import TreeNode
from typing import Optional
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1

        self.dfs(root, 0, targetSum)

        return self.total

    def dfs(self, node: TreeNode, root_sum: int, targetSum: int):
        if not node:
            return
        root_sum += node.val

        self.total += self.lookup[root_sum]
        self.lookup[root_sum+targetSum] += 1

        self.dfs(node.left, root_sum, targetSum)
        self.dfs(node.right, root_sum, targetSum)

        self.lookup[root_sum+targetSum] -= 1


if __name__ == "__main__":
    root = TreeNode.build_binary_tree(
        [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    targetSum = 8

    s = Solution()
    print(s.pathSum(root, targetSum))
