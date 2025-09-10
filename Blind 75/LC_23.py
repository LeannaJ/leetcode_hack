# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq  # min-heap utilities

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
         """
        Merge k sorted linked lists and return it as one sorted list.

        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Create a min-heap to always pop the smallest current node among lists
        heap = []  # will store tuples: (node value, tie-breaker, node reference)

        # Initialize the heap with the head of each non-empty list
        for node in lists:                       # iterate over each head node
            if node is not None:                 # skip empty lists
                heapq.heappush(heap, (node.val, id(node), node))  # push tuple

        # Dummy head to simplify list construction
        dummy = ListNode(0)   # sentinel node for result list
        tail = dummy          # tail pointer for appending nodes

        # Extract the smallest node, then push its next node (if exists)
        while heap:                                   # while we have nodes in heap
            _, _, smallest = heapq.heappop(heap)      # pop the smallest-value node
            tail.next = smallest                      # append to result list
            tail = tail.next                          # advance tail
            if smallest.next is not None:             # if there is a successor
                nxt = smallest.next                   # cache next node
                heapq.heappush(heap, (nxt.val, id(nxt), nxt))  # push successor

        # Return the merged list (skip dummy sentinel)
        return dummy.next


# CoderPad/HackerRank Test
from typing import List, Optional, Iterable, Tuple
import heapq

# Linked list utilities
class ListNode:
    # Node of singly linked list
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val                           # store node value
        self.next = next                         # pointer to next node

    def __repr__(self):
        # Helpful for debugging in CoderPad
        return f"ListNode(val={self.val})"

def build_list(values: Iterable[int]) -> Optional[ListNode]:
    # Convert a Python iterable of ints into a linked list; return head
    dummy = ListNode(0)                          # sentinel to simplify append
    tail = dummy                                 # tail pointer for building
    for v in values:                             # iterate input values
        tail.next = ListNode(v)                  # create and link a new node
        tail = tail.next                         # move tail forward
    return dummy.next                            # head is after dummy

def list_to_array(head: Optional[ListNode]) -> List[int]:
    # Convert a linked list back to Python list (for testing/printing)
    out = []                                     # accumulator list
    cur = head                                   # start from head
    while cur is not None:                       # traverse list
        out.append(cur.val)                      # collect value
        cur = cur.next                           # move forward
    return out                                   # return collected values

# Merge k lists with min-heap
def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Defensive checks for common edge cases
    if lists is None:                            # handle None input (rare but defensive)
        return None
    if len(lists) == 0:                          # k == 0
        return None
    if len(lists) == 1:                          # single list: already merged
        return lists[0]

    # Build a heap from the head of each non-empty list
    heap: List[Tuple[int, int, ListNode]] = []   # (value, tie-breaker, node)
    for node in lists:                           # iterate over provided heads
        if node is not None:                     # skip empty lists
            heapq.heappush(heap, (node.val, id(node), node))  # push to heap

    # If all lists were empty -> return None
    if not heap:                                 # heap empty means no nodes at all
        return None

    # Prepare a dummy head for the merged result
    dummy = ListNode(0)                          # sentinel for result
    tail = dummy                                 # tail pointer to append nodes

    # Merge by continuously popping the smallest node and pushing its next
    while heap:                                  # process until heap is empty
        _, _, smallest = heapq.heappop(heap)     # get node with minimum value
        tail.next = smallest                     # append to merged list
        tail = tail.next                         # advance tail
        if smallest.next is not None:            # if more nodes remain in this list
            nxt = smallest.next                  # cache the next node
            heapq.heappush(heap, (nxt.val, id(nxt), nxt))  # push next node

    # Ensure the final list ends properly (tail.next already points correctly)
    return dummy.next                            # return head of merged list

# Simple demo / tests (can be run in CoderPad)
if __name__ == "__main__":
    # Build sample inputs: [[1,4,5],[1,3,4],[2,6]]
    lists = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6])
    ]
    merged = merge_k_lists(lists)
    print(list_to_array(merged))  # Expected: [1,1,2,3,4,4,5,6]

    # Edge cases
    print(list_to_array(merge_k_lists([])))                        # k = 0 -> []
    print(list_to_array(merge_k_lists([None, None])))              # all empty -> []
    print(list_to_array(merge_k_lists([build_list([-3, -1, 2])])) )# single list -> [-3,-1,2]
    print(list_to_array(merge_k_lists([build_list([1,1]), build_list([1])])) ) # duplicates
        