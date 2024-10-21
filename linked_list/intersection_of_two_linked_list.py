from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        while A != B:
            if not A:
                A = headB
            else:
                A = A.next
            if not B:
                B = headA
            else:
                B = B.next
        return A


# Test case
if __name__ == "__main__":
    arr1 = [4, 1, 8, 10, 1]
    arr2 = [5, 6, 1, 8, 2, 11]

    head1 = array_to_linked_list(arr1)
    head2 = array_to_linked_list(arr2)

    solution = Solution()
    head = solution.getIntersectionNode(head1, head2)

    print(print_linked_list(head))
