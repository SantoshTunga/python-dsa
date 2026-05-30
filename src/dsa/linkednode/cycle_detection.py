from dsa.linkednode import linked_node
from linked_node import LinkedNode


def detect_cycle(head: LinkedNode | None) -> bool:
    slow = head
    fast = head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if fast is slow:
            return True
    return False


def get_cycle_node(head: LinkedNode | None) -> LinkedNode | None:
    slow = head
    fast = head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if fast is slow:
            fast = head
            while slow is not fast:
                slow = slow.next_node
                fast = fast.next_node
            return slow
    return None


if __name__ == '__main__':
    first_node = linked_node.construct_cycle_linked_node()
    print(detect_cycle(first_node))
    first_node = linked_node.construct_cycle_linked_node()
    node = get_cycle_node(first_node)

    if node:
        print(f" cycle node value = {node.value} ")
    else:
        print("no cycle found")
