from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":

    l1 = [1, 2, 3, 4, 5, 6]
    head_1 = array_to_linked_list(l1)

    solution = Solution()

    res = solution.middleNode(head_1)

    print_linked_list(res)
