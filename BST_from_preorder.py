class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def subsets_bst(arr):
    root = arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i] > root:
            index = i
            break
            # return first_ele_value_right_bst, i
    subset_left_bst = arr[1:index]
    subset_right_bst = arr[index:len(arr)]
    return subset_left_bst, subset_right_bst


def insert(root, node):
    if root is None:
        root = node
    if root.value < node.value:
        if root.right is None:
            root.right = node
        else:
            insert(root.right,node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left,node)


def generate_bst(arr):
    if not len(arr):
        return None
    else:
        root = Node(arr[0])
        arr_left_bst, arr_right_bst = subsets_bst(arr)
        for k in range(len(arr_left_bst)):
            node = Node(arr_left_bst[k])
            insert(root, node)
        for k in range(len(arr_right_bst)):
            node = Node(arr_right_bst[k])
            insert(root, node)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
    else:
        return None


pre = [10, 5, 1, 7, 40, 50]
root = generate_bst(pre)
inorder(root)





