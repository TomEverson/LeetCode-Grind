from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l1 = self.reverse_linked_list(head)
        dummy = l1

        carry = 0
        while dummy:
            product = (dummy.val * 2) + carry
            carry = product // 10
            dummy.val = product % 10
            dummy = dummy.next

        l1 = self.reverse_linked_list(l1, carry)

        return l1

    def reverse_linked_list(self, head: Optional[ListNode], carry=None) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if carry:
            dummy = ListNode(carry)
            dummy.next = prev
            return dummy
        else:
            return prev


if __name__ == "__main__":

    s = Solution()

    l1 = [9, 8, 9]
    l1 = array_to_linked_list(l1)

    print_linked_list(s.doubleIt(l1))
