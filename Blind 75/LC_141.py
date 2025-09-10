# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional['ListNode']) -> bool:
        # Edge case: empty list or single node -> no cycle possible
        if head is None or head.next is None:
            return False
        
        # Initialize two pointers
        slow = head          # moves 1 step at a time
        fast = head.next     # moves 2 steps at a time (start ahead to simplify equality check)
        
        # Traverse until pointers meet or fast reaches the end
        while slow is not fast:
            # If fast hits the end, there is no cycle
            if fast is None or fast.next is None:
                return False
            # Move slow by 1 and fast by 2
            slow = slow.next
            fast = fast.next.next
        
        # If slow == fast, a cycle exists
        return True


# CoderPad/HackerRank Test
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    # Edge case: empty list or single node
    if head is None or head.next is None:
        return False
    
    slow = head
    fast = head.next
    
    while slow is not fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True

# --------- Quick sanity tests ---------
# Build small lists directly during interview
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
print(has_cycle(a))  # False

# Make a cycle: c -> b
c.next = b
print(has_cycle(a))  # True

# Single node, no cycle
x = ListNode(42)
print(has_cycle(x))  # False

# Single node, self loop
y = ListNode(99)
y.next = y
print(has_cycle(y))  # True