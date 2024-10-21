from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry

            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


if __name__ == "__main__":

    solution = Solution()

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    head_1 = array_to_linked_list(l1)
    head_2 = array_to_linked_list(l2)

    s = solution.addTwoNumbers(head_1, head_2)

    print(print_linked_list(s))
