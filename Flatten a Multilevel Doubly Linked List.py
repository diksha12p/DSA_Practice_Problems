"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
which may or may not point to a separate doubly linked list. These child lists may have one or more children of their
own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the
first level of the list.

1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL


The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

Output: [1,2,3,7,8,11,12,9,10,4,5,6]
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack, curr = [], head
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next, curr.child.prev = curr.child, curr
                curr.child = None
            if not curr.next and stack:
                curr_node = stack.pop()
                curr_node.prev, curr.next = curr, curr_node
            curr = curr.next
        return head



