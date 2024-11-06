from typing import Optional
from utils import TreeNode
from collections import deque

#! DFS + Recursion


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.right))

#! BFS ( Iterative )
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         level = 0
#         q = deque([root])

#         while q:
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)

#                 level += 1

#         return level

#! DFS + Stack ( Iterative )
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

#         stack = [[root, 1]]
#         res = 1

#         while stack:
#             node, depth = stack.pop()

#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, depth + 1])
#                 stack.append([node.right, depth + 1])
#         return res


if __name__ == "__main__":

    solution = Solution()

    tree = TreeNode.build_binary_tree(
        [3, 9, 20, None, None, 15, 7, None, None, 21])

    tree.display()

    depth = solution.maxDepth(tree)

    print(depth)
