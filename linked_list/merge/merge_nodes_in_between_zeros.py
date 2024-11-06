from utils import ListNode, print_linked_list, array_to_linked_list
from typing import Optional


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        curr = dummy

        while curr.next:
            while curr.next.val != 0:
                curr.val += curr.next.val
                curr.next = curr.next.next

            if curr.next.val == 0:
                if curr.next.next:
                    curr = curr.next
                else:
                    curr.next = None

        return dummy


if __name__ == "__main__":

    s = Solution()

    l1 = [0, 1, 0, 3, 0, 2, 2, 0]
    l1 = array_to_linked_list(l1)

    print_linked_list(s.mergeNodes(l1))
