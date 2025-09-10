# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

class LRUCache:
    class _Node:
        # Doubly linked list node to store key and value
        def __init__(self, key: int, value: int):
            self.key = key                 # store key to allow removal from dict on eviction
            self.value = value             # store value
            self.prev = None               # pointer to previous node
            self.next = None               # pointer to next node

    def __init__(self, capacity: int):
        # Initialize capacity and core data structures
        self.capacity = capacity                      # maximum number of entries allowed
        self.map = {}                                 # key -> _Node (for O(1) lookup)
        # Create dummy head and tail to simplify edge operations
        self.head = self._Node(0, 0)                  # dummy head (MRU side)
        self.tail = self._Node(0, 0)                  # dummy tail (LRU side)
        self.head.next = self.tail                    # link head -> tail
        self.tail.prev = self.head                    # link tail -> head

    # ---- Internal helper methods for list ops (all O(1)) ----
    def _add_to_front(self, node):
        # Insert 'node' right after head (mark as most recently used)
        node.prev = self.head                         # node's prev becomes head
        node.next = self.head.next                    # node's next becomes old first node
        self.head.next.prev = node                    # fix back pointer of old first node
        self.head.next = node                         # head now points to node

    def _remove_node(self, node):
        # Detach 'node' from its current position
        prev_node = node.prev                         # keep reference to previous node
        next_node = node.next                         # keep reference to next node
        prev_node.next = next_node                    # bridge previous to next
        next_node.prev = prev_node                    # bridge next back to previous
        node.prev = node.next = None                  # optional: help GC / avoid misuse

    def _move_to_front(self, node):
        # Move an existing node to the front (MRU position)
        self._remove_node(node)                       # detach node from current spot
        self._add_to_front(node)                      # re-insert right after head

    def _evict_from_tail(self):
        # Remove least recently used node (the one before tail)
        lru = self.tail.prev                          # lru candidate (before dummy tail)
        self._remove_node(lru)                        # cut it from the list
        del self.map[lru.key]                         # remove from hashmap as well

    # ---- Public API ----
    def get(self, key: int) -> int:
        # Return value if key exists, else -1; mark as most recently used
        if key not in self.map:                       # key not cached
            return -1                                 # requirement: return -1
        node = self.map[key]                          # fetch node in O(1)
        self._move_to_front(node)                     # mark as recently used
        return node.value                             # return stored value

    def put(self, key: int, value: int) -> None:
        # Insert or update; if over capacity, evict LRU
        if key in self.map:                           # updating existing key
            node = self.map[key]                      # fetch node
            node.value = value                        # update value
            self._move_to_front(node)                 # mark as recently used
            return                                    # done

        # Insert a brand new key
        if self.capacity == 0:                        # degenerate case: no storage allowed
            return                                    # do nothing as per many LC discussions

        new_node = self._Node(key, value)             # create node for the pair
        self.map[key] = new_node                      # index in hashmap
        self._add_to_front(new_node)                  # add as most recently used

        if len(self.map) > self.capacity:             # capacity exceeded?
            self._evict_from_tail()                   # evict one LRU


# CoderPad/HackerRank Test
class LRUCache:
    class _Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = self._Node(0, 0)   # dummy head
        self.tail = self._Node(0, 0)   # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_front(node)

    def _evict(self):
        lru = self.tail.prev
        self._remove(lru)
        del self.map[lru.key]

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.map) >= self.capacity:
                self._evict()
            node = self._Node(key, value)
            self.map[key] = node
            self._add_to_front(node)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))   # expect 1
cache.put(3, 3)       # evicts key 2
print(cache.get(2))   # expect -1
cache.put(4, 4)       # evicts key 1
print(cache.get(1))   # expect -1
print(cache.get(3))   # expect 3
print(cache.get(4))   # expect 4