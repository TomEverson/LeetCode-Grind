from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        front = None
        end = None
        curr = head

        while curr:
            count += 1

            if count == k:
                front = curr
                end = head

            if count > k:
                end = end.next

            curr = curr.next

        temp = front.val
        front.val = end.val
        end.val = temp

        return head


if __name__ == "__main__":
    s = Solution()

    head = [1, 2, 3, 4, 5]
    k = 2

    head = array_to_linked_list(head)
    print_linked_list(s.swapNodes(head, k))
