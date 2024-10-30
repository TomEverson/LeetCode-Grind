from utils import TreeNode
from typing import Optional
from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)
            sum = 0

            for _ in range(level_size):
                node = queue.popleft()

                sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(sum)

        return 1 + res.index(max(res))


if __name__ == "__main__":
    l1 = TreeNode.build_binary_tree([1, 7, 0, 7, -8, None, None])

    s = Solution()
    print(s.maxLevelSum(l1))
