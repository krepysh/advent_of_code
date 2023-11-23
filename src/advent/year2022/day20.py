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

mod = len(nodes) - 1
for i in range(len(nodes)):
    node = nodes[i]
    node.left = nodes[i - 1]
    node.right = nodes[(i + 1) % len(nodes)]


for node in nodes:
    if node.val == 0:
        zero = node
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
        print('error')
        continue
    print(f'{node.val} moves between {left.val} and {right.val}:')
    # Cut node from initial position by linking neighbours to each other:
    node.left.right, node.right.left = node.right, node.left
    # Connect the node to the left neighbour:
    node.left = left
    left.right = node
    # Connect the node to the right neighbour:
    node.right = right
    right.left = node

# checking that length is correct
ll_len = 1
start = zero.right
while start.val != zero.val:
    ll_len += 1
    start = start.right
print(f'Len of linked list: {ll_len}')


# Calculate grove coordinates part 1
res = 0
for shift in (1000, 2000, 3000):
    coord = zero
    for _ in range(shift):
        coord = coord.right
    num = coord.val
    print(num)
    res += num

print(res)
