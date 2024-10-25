from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse_list(head)

        curr = l1
        maxSeen = curr.val

        while curr.next:
            if curr.next.val < maxSeen:
                curr.next = curr.next.next
            else:
                maxSeen = curr.next.val
                curr = curr.next

        l1 = self.reverse_list(l1)

        return l1

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


if __name__ == "__main__":
    s = Solution()
    l1 = array_to_linked_list([1, 1, 1, 1])

    s.removeNodes(l1)
