from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    l1 = [6, 1, 3, 1, 6]
    l1 = array_to_linked_list(l1)

    print_linked_list(s.removeElements(l1, 6))
