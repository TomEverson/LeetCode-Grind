from utils import ListNode, print_linked_list, array_to_linked_list
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, current = None, slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


if __name__ == "__main__":

    s = Solution()

    l1 = [1, 2, 2, 1]
    l1 = array_to_linked_list(l1)

    print(s.isPalindrome(l1))
