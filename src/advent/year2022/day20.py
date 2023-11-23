from advent import read_input


class ListNode:
    def __init__(self, val):
        self.val = int(val)
        self.left: ListNode = None
        self.right: ListNode = None


nodes: list[ListNode] = read_input('day20.txt', convert_to=ListNode)

vals = [-6, 2, -3, 3, -2, 0, 4]

# Create nodes and form a circular doubly linked list
# nodes = [ListNode(val) for val in vals]


def prepare_nodes(nodes: list[ListNode], multiplicator=1) -> ListNode:
    for i in range(len(nodes)):
        node = nodes[i]
        node.val = node.val * multiplicator
        node.left = nodes[i - 1]
        node.right = nodes[(i + 1) % len(nodes)]
        if node.val == 0:
            zero = node
    return zero


def mix(nodes: list[ListNode]):
    mod = len(nodes) - 1
    debug = len(nodes) < 15
    for node in nodes:
        if node.val == 0:
            continue
        left = node
        if node.val > 0:
            for _ in range(node.val % mod):
                left = left.right
        else:
            for _ in range((1 + abs(node.val)) % mod):
                left = left.left
        right = left.right
        if left == node or right == node:
            continue
        if debug:
            print(f'{node.val} moves between {left.val} and {right.val}:')
        # Cut node from initial position by linking neighbours to each other:
        node.left.right, node.right.left = node.right, node.left
        # Connect the node to the left neighbour:
        node.left = left
        left.right = node
        # Connect the node to the right neighbour:
        node.right = right
        right.left = node


def check_linked_list_len(start_from):
    # checking that length is correct
    ll_len = 1
    start = start_from.right
    while start.val != start_from.val:
        ll_len += 1
        start = start.right
    return ll_len


# Calculate grove coordinates part 1
zero = prepare_nodes(nodes)
mix(nodes)
assert check_linked_list_len(zero) == 5000
res = 0
for shift in (1000, 2000, 3000):
    coord = zero
    for _ in range(shift):
        coord = coord.right
    num = coord.val
    print(num)
    res += num

print(res)

# part 2

nodes: list[ListNode] = read_input('day20.txt', convert_to=ListNode)
zero = prepare_nodes(nodes, multiplicator=811589153)
for round_number in range(10):
    mix(nodes)
assert check_linked_list_len(zero) == 5000
res = 0
for shift in (1000, 2000, 3000):
    coord = zero
    for _ in range(shift):
        coord = coord.right
    num = coord.val
    res += num
print(res)
