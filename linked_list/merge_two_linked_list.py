from utils import ListNode, array_to_linked_list, print_linked_list


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return dummy.next


solution = Solution()

# Test case
if __name__ == "__main__":

    list_one = array_to_linked_list([1, 2, 4])
    list_two = array_to_linked_list([1, 3, 4])

    solution = Solution()
    reversed_head = solution.mergeTwoLists(list_one, list_two)

    print_linked_list(reversed_head)
