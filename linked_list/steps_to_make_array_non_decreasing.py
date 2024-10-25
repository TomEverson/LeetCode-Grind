from utils import ListNode, print_linked_list, array_to_linked_list
from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        return


if __name__ == "__main__":
    l1 = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]
    l1 = array_to_linked_list(l1)

    s = Solution()

    print_linked_list(s.totalSteps(l1))
