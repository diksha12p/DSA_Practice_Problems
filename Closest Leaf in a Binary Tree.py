
"""
"# Python program to find the closest leaf in a binary tree



                                 1
                               /  \
                              2    3
                            /  \
                          4     5
                         /    /  \
                        8    10  11
                       /    /     \
                      7    12     15
# in the above tree closest leaf node is 3 at distance 1.
# to find the closest leaf node we just traverse the tree in normal fashion
# and check distance for every leaf node
"""


class new_node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BT(object):
    def __init__(self,root):
        self.root=root

    def Find_Closest(self, node, l, dmin):
        """
        this function will return the min distance and leaf value
        and will store them in dmin array """

        # base case
        if not node:
            return
        # if current node is leaf node
        if not node.left and not node.right:
            if l<dmin[0]:
                dmin[0]=l
                dmin[1]=node

        print(dmin)
        # reccur for leaf and right subtree
        self.Find_Closest(node.left, l + 1, dmin)
        self.Find_Closest(node.right, l + 1, dmin)

    def Print_leaf(self):
        dmin=[100]*2
        self.Find_Closest(self.root,0,dmin)
        return dmin[0],dmin[1].value


if __name__=="__main__":
        root=new_node(1)

        root.left=new_node(2)
        root.right=new_node(3)

        root.left.left=new_node(4)
        root.left.right=new_node(5)
        root.left.left.left=new_node(8)
        root.left.left.left.left=new_node(7)

        root.left.right.left=new_node(10)
        root.left.right.right=new_node(11)
        root.left.right.left.left=new_node(12)
        root.left.right.right.right=new_node(15)

        obj=BT(root)
        distance,leaf=obj.Print_leaf()
        print("closest leaf node from root is %d at distance %d " %(leaf,distance))

        '''
        output::  closest leaf node from root is 3 at distance 1
        time complexity is O(n)
        where n=number of nodes in the binary tree'''