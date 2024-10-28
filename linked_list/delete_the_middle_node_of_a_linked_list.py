from typing import Optional
from utils import ListNode, array_to_linked_list, print_linked_list


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head


if __name__ == "__main__":
    l1 = array_to_linked_list([1, 3, 4, 7, 1, 2, 6])

    s = Solution()
    print_linked_list(s.deleteMiddle(l1))
