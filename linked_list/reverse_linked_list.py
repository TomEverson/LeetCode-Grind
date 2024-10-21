from utils import ListNode, array_to_linked_list, print_linked_list


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


# Test case
if __name__ == "__main__":
    arr = [1, 2, 3]

    head = array_to_linked_list(arr)

    solution = Solution()
    reversed_head = solution.reverseList(head)

    print(print_linked_list(reversed_head))
