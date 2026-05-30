class LinkedNode:
    def __init__(self, value: int, next_node: LinkedNode | None = None):
        self.value = value
        self.next_node = next_node


def construct_linked_node() -> LinkedNode:
    l5 = LinkedNode(5)
    l4 = LinkedNode(4, l5)
    l4 = LinkedNode(4, l5)
    l3 = LinkedNode(3, l4)
    l2 = LinkedNode(2, l3)
    l1 = LinkedNode(1, l2)
    return l1


def construct_cycle_linked_node() -> LinkedNode:
    l5 = LinkedNode(5)
    l4 = LinkedNode(4, l5)
    l3 = LinkedNode(3, l4)
    l5.next_node = l3
    l2 = LinkedNode(2, l3)
    l1 = LinkedNode(1, l2)
    return l1


def print_linked_node(node: LinkedNode | None):
    while node:
        print(f"node value = {node.value}")
        node = node.next_node


if __name__ == '__main__':
    head = construct_linked_node()
    print_linked_node(head)
