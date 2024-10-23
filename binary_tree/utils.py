from typing import List, Optional


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = left
        self.left = right

    def insert(self, val):
        queue = [self]
        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = TreeNode(val)
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = TreeNode(val)
                return
            else:
                queue.append(current.right)

    @classmethod
    def build_binary_tree(cls, val: List[any]) -> "TreeNode":
        if not val:
            return None

        root = cls(val[0])  # Create the root node
        queue = [root]  # Use a queue to insert children in level-order
        index = 1  # Start inserting from the second element

        while queue and index < len(val):
            current = queue.pop(0)  # Dequeue the front node

            # Insert left child
            if index < len(val) and val[index] is not None:
                current.left = cls(val[index])
                queue.append(current.left)
            index += 1  # Move to the next index

            # Insert right child
            if index < len(val) and val[index] is not None:
                current.right = cls(val[index])
                queue.append(current.right)
            index += 1  # Move to the next index

        return root

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""

        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
