class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


def create_cycle_linked_list(arr, pos):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    cycle_node = None

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        if i == pos:
            cycle_node = current

    current.next = cycle_node

    return head
