from utils import ListNode, array_to_linked_list, print_linked_list
from typing import Optional, List


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        dummy = head

        curr = dummy

        critical_point = []

        idx = 2

        while curr.next.next:
            if curr.val > curr.next.val and curr.next.val < curr.next.next.val or curr.val < curr.next.val and curr.next.val > curr.next.next.val:
                critical_point.append(idx)

            idx += 1
            curr = curr.next

        if not critical_point or len(critical_point) == 1:
            return [-1, -1]

        min_distance = float("inf")
        max_distance = critical_point[-1] - critical_point[0]

        for i in range(1, len(critical_point)):
            min_distance = min(
                min_distance, critical_point[i] - critical_point[i - 1])

        return [min_distance, max_distance]


if __name__ == "__main__":
    l1 = [6, 8, 4, 1, 9, 6, 6, 10, 6]

    l1 = array_to_linked_list(l1)

    s = Solution()

    print(s.nodesBetweenCriticalPoints(l1))
