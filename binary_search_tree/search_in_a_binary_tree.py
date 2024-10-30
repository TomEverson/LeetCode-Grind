from utils import TreeNode
from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root

        while current:
            if current.val > val:
                current = current.left
            elif current.val < val:
                current = current.right
            else:
                return current


if __name__ == "__main__":
    l1 = TreeNode.build_binary_tree([4, 2, 7, 1, 3])

    s = Solution()
    l1 = s.searchBST(l1, 2)

    l1.display()
