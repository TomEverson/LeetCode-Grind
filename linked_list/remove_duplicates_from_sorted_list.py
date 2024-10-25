from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head

        while dummy and dummy.next:
            if dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return head


if __name__ == "__main__":
    s = Solution()
    l1 = array_to_linked_list([1, 1, 2])
    l1 = s.deleteDuplicates(l1)

    print_linked_list(l1)
