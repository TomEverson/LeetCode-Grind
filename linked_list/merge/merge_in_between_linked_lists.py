from utils import ListNode, array_to_linked_list, print_linked_list


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        end = list2
        temp = None
        current = list1

        index = 1

        while current:
            if a <= index <= b:
                current.next = current.next.next
            elif index > b:
                temp = current.next

                while end:
                    if not end.next:
                        end.next = temp
                        break
                    end = end.next

                current.next = list2

                break

            else:
                current = current.next
            index += 1

        return list1


if __name__ == "__main__":

    s = Solution()

    l1 = array_to_linked_list([0, 1, 2, 3, 4, 5, 6])
    l2 = array_to_linked_list([1000000, 1000001, 1000002, 1000003, 1000004])

    print_linked_list(s.mergeInBetween(l1, 2, 5, l2))
