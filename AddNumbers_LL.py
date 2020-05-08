class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self,l1, l2):
        root = ans = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, val = divmod(val1 + val2 + carry, 10)
            ans.next = ListNode(val)
            ans = ans.next
        return root.next









