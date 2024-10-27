from utils import TreeNode


class Solution:

    #! Recursive
    # def hightOfBinarySearchTree(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return -1

    #     left = self.hightOfBinarySearchTree(root.left)
    #     right = self.hightOfBinarySearchTree(root.right)

    #     return max(left, right) + 1

    #! Iterative
    def hightOfBinarySearchTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return -1

        max_height = 0
        stack = [(root, 0)]

        while stack:
            node, current_height = stack.pop()

            if node:
                max_height = max(max_height, current_height)
                stack.append((node.left, current_height + 1))
                stack.append((node.right, current_height + 1))

        return stack


if __name__ == "__main__":
    l1 = TreeNode.build_binary_tree(
        [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85, 5, 15, 27, 37, 47, 57, 67, 77, 87, 1])

    s = Solution()
    res = s.hightOfBinarySearchTree(l1)

    print(res)
