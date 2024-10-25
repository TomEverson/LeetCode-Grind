from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = head

        slow, fast = head, head

        res = []

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverse(slow)

        while slow:
            res.append(dummy.val + slow.val)
            dummy = dummy.next
            slow = slow.next

        return max(res)

    def reverse(self, head: Optional[ListNode]) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


if __name__ == "__main__":
    s = Solution()

    l1 = array_to_linked_list([4, 2, 2, 3])

    print(s.pairSum(l1))
