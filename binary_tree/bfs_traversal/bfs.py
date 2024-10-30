from utils import TreeNode
from typing import Optional
from collections import deque


class Solution:
    def bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res


if __name__ == "__main__":
    l1 = [3, 9, 20, None, None, 15, 7]
    l1 = TreeNode.build_binary_tree(l1)

    s = Solution()
    print(s.bfs(l1))
