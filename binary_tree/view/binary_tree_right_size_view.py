from utils import TreeNode
from typing import List, Optional
from collections import deque


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            right_view = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    right_view = node
                    q.append(node.left)
                    q.append(node.right)

            if right_view:
                res.append(right_view.val)
        return res


if __name__ == "__main__":
    l1 = [1, 2]
    solution = Solution()
    tree = TreeNode.build_binary_tree(l1)

    print(solution.rightSideView(tree))
