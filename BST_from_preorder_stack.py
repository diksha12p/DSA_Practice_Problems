class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def gen_bst_using_stack(pre_array):
    stack = []
    root = Node(pre_array[0])
    stack.append(root)
    for i in range(1, len(pre_array)):
        temp = None
        # print("for i ={}, value of pre[i] = {} and top of stack is ={}".format(i, pre[i], stack[-1].value))

        if pre_array[i] < stack[-1].value:
            temp = stack[-1]
            # print("Current value of temp is {}".format(temp.value))
            temp.left = Node(pre_array[i])
            stack.append(temp.left)

        else:
            while len(stack) and pre_array[i] > stack[-1].value:
                # print("while loop")
                temp = stack.pop()
                # print("Current value of temp is {}".format(temp.value))

            if temp is not None:
                temp.right = Node(pre_array[i])
                stack.append(temp.right)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end= "    ")
        inorder(root.right)
    else:
        return None


pre = [10, 5, 1, 7, 40, 50]
inorder(gen_bst_using_stack(pre))




