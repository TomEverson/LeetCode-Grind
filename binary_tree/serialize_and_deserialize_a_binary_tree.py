from utils import TreeNode
from collections import deque


class Codec:

    def serialize(self, root):
        if not root:
            return ""

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            if values[i] != "#":
                leftNode = TreeNode(int(values[i]))
                node.left = leftNode
                queue.append(leftNode)
            i += 1

            if values[i] != "#":
                rightNode = TreeNode(int(values[i]))
                node.right = rightNode
                queue.append(rightNode)
            i += 1

        return root


if __name__ == "__main__":
    tree = TreeNode.build_binary_tree([1, 2, 3, None, None, 4, 5])

    s = Codec()

    print(s.serialize(tree))

    tree_2 = s.deserialize("1,2,3,#,#,4,5,#,#,#,#")

    tree_2.display()
