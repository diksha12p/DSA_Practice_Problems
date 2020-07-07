"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

# IDEA 1 : Use a Doubly Linked List for O(1) Insertion and Deletion
# Use an extra data structure -> Hash Map (dict) to ensure the 'get' operation in O(1)
# hash map => {key : Node}


from collections import OrderedDict


class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = dict()

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.d:
            return -1
        curr_node = self.d[key]
        self._remove(curr_node)
        self._add(curr_node)

        return curr_node.val

    def put(self, key, value):
        if key in self.d:
            self._remove(self.d[key])
        node = Node(key, value)
        self._add(node)
        self.d[key] = node

        if len(self.d) > self.capacity:
            curr_node = self.head.next
            self._remove(curr_node)
            del self.d[curr_node.key]

    def _remove(self, node):
        n_prev = node.prev
        n_next = node.next
        n_prev.next = n_next
        n_next.prev = n_prev

    def _add(self, node):
        n_prev = self.tail.prev
        n_prev.next = node
        self.tail.prev = node
        node.prev = n_prev
        node.next = self.tail


# IDEA 2: Use an Ordered Dict which as Doubly Linked List as its underlying implementation
# Ordered Dict: Preserves the order in which keys were first inserted

class LRU_Cache_OrderedDict:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)





