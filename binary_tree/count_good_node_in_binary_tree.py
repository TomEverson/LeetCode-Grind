from utils import TreeNode


class Solution:

    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.count

    def dfs(self, root: TreeNode, val=float("-inf")):
        if not root:
            return

        if root.val >= val:
            self.count += 1
            val = root.val

        self.dfs(root.left, val)
        self.dfs(root.right, val)


if __name__ == "__main__":
    l1 = [-1, 5, -2, 4, 4, 2, -2, None, None, -4, None, -2, 3, None, -2, 0, None, -
          1, None, -3, None, -4, -3, 3, None, None, None, None, None, None, None, 3, -3]

    tree = TreeNode.build_binary_tree(l1)

    s = Solution()

    print(s.goodNodes(tree))
