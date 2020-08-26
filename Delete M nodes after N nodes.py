class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def skip_M_del_N(self, M, N):
        curr = self.head
        while curr:
            for count in range(1, M):
                if curr is None:
                    return
                curr = curr.next

            if curr is None:
                return

            trav = curr.next
            for count in range(1, N+1):
                if trav is None:
                    break
                trav = trav.next

            curr.next = trav.next
            curr = trav
        return self.head

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # Traverse till last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        # Make the new node the last node
        last_node.next = new_node

    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.next.val, " ->", end=" ")
            temp = temp.next
        print("/")

if __name__ == '__main__':
    ll = LinkedList()

    for i in range(11):
        ll.add_node(i)

    ll.print_list()
    print("\n")

    ll.skip_M_del_N(3, 2)
    ll.print_list()
