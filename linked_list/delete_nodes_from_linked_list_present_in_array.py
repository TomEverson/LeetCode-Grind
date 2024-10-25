from utils import ListNode, array_to_linked_list, print_linked_list
from typing import List, Optional


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current and current.next:
            if current.next.val in num_set:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next


if __name__ == "__main__":

    s = Solution()

    head = array_to_linked_list([1, 2, 3, 4, 5])
    nums = [1, 2, 3]

    new_head = s.modifiedList(nums, head)

    print_linked_list(new_head)
