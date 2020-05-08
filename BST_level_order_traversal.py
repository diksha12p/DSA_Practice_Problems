class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order_traversal(root):
    if root is None:
        return

    queue = list()
    queue.append(root)
    # print(queue[0].value)
    while len(queue) > 0:
        print(queue[0].value, end= "    ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


# Driver Program to test above function
root = Node(10)
root.left = Node(2)
root.right = Node(12)
root.left.left = Node(4)
root.left.right = Node(5)

# pre = [10, 5, 1, 7, 40, 50]
# root = Node(pre[0])
level_order_traversal(root)


