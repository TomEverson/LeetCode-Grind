from typing import Optional
from utils import ListNode, array_to_linked_list, print_linked_list


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == "__main__":
    l1 = array_to_linked_list([1, 2, 3, 4, 5])
    s = Solution()
    print_linked_list(s.oddEvenList(l1))
