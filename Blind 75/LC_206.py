# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        prev = None                   # 'prev' will trail behind and become the new head
        curr = head                   # 'curr' walks through the list
        
        while curr:                   # iterate until we run off the list
            nxt = curr.next           # save next node before we break the link
            curr.next = prev          # reverse the pointer
            prev = curr               # move 'prev' forward
            curr = nxt                # move 'curr' forward using saved next
            
        return prev                   # 'prev' is the new head

    
# CoderPad/HackerRank Test
from typing import Optional, Iterable

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val               # store the node's value
        self.next = next             # pointer to the next node

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list iteratively in O(N) time and O(1) space."""
    prev = None                      # 'prev' will trail and form the reversed part
    curr = head                      # 'curr' traverses the original list
    
    while curr is not None:          # continue until the end of list
        nxt = curr.next              # keep reference to the next node
        curr.next = prev             # reverse the link
        prev = curr                  # advance 'prev' to current
        curr = nxt                   # advance 'curr' to saved next
    
    return prev                      # 'prev' is the new head of the reversed list

# Helper functions
def build_list(values: Iterable[int]) -> Optional[ListNode]:
    """Build a linked list from an iterable of ints and return head."""
    dummy = ListNode(0)              # dummy head to simplify insertions
    tail = dummy                     # 'tail' points to the last node
    for v in values:                 # iterate through provided values
        tail.next = ListNode(v)      # append new node
        tail = tail.next             # move tail forward
    return dummy.next                # skip dummy and return real head

def to_array(head: Optional[ListNode]) -> list:
    """Convert linked list to Python list for quick checks."""
    out = []                         # container for values
    curr = head                      # start from head
    # Safety bound to avoid infinite loops if a cycle mistakenly appears
    steps = 0                        # step counter
    while curr is not None and steps <= 100000: # hard cap for safety
        out.append(curr.val)         # collect value
        curr = curr.next             # move forward
        steps += 1                   # increment step count
    return out                       # return collected values

# Quick sanity tests (can be commented out in interviews)
if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])  # create 1->2->3->4->5
    rev  = reverse_list(head)           # reverse it
    print(to_array(rev))                # expected: [5, 4, 3, 2, 1]