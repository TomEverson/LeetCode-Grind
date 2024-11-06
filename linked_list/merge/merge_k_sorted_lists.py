from utils import ListNode, array_to_linked_list, print_linked_list
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])

        return lists[-1]

    def mergeList(self, l1: ListNode, l2: ListNode) -> ListNode:

        node = dummy = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1:
            node.next = l1

        if l2:
            node.next = l2

        return dummy.next


s = Solution()

print_linked_list(s.mergeKLists([[1, 2, 4], [1, 3, 5], [3, 6]]))
