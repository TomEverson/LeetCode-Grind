from utils import ListNode, create_cycle_linked_list, print_linked_list
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    l1 = [3, 2, 0, -4]
    pos = 2

    solution = Solution()

    head = create_cycle_linked_list(l1, pos)

    res = solution.hasCycle(head)

    print(res)
