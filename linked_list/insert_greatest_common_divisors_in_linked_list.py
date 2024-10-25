from utils import ListNode, print_linked_list, array_to_linked_list
from typing import Optional


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head

        curr = dummy

        while curr.next:
            temp = curr.next
            common_d = self.gcd(curr.val, curr.next.val)
            new_node = ListNode(common_d)
            new_node.next = temp
            curr.next = new_node
            curr = temp

        return dummy

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a


if __name__ == "__main__":
    s = Solution()

    l1 = array_to_linked_list([18, 6, 10, 3])

    print_linked_list(s.insertGreatestCommonDivisors(l1))
