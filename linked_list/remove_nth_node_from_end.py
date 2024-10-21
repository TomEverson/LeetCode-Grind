from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    n = 2

    head = array_to_linked_list(array)

    solution = Solution()

    print(print_linked_list(solution.removeNthFromEnd(head, n)))
