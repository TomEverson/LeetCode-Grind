from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        prev, curr = None, head
        res = 0
        power = 0

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev:
            if prev.val == 1:
                res += (2 ** power)

            power += 1
            prev = prev.next

        return res


if __name__ == "__main__":
    s = Solution()

    l1 = [1, 0, 1]
    l1 = array_to_linked_list(l1)

    print(s.getDecimalValue(l1))
