# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify list construction
        dummy = ListNode(-1)
        current = dummy  # pointer to build the new list
        
        # While both lists are non-empty
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # attach list1 node
                list1 = list1.next    # move list1 forward
            else:
                current.next = list2  # attach list2 node
                list2 = list2.next    # move list2 forward
            current = current.next    # move the builder forward
        
        # Attach the remaining nodes from either list1 or list2
        current.next = list1 if list1 else list2
        
        return dummy.next  # return the merged list (skip dummy)


# CoderPad/HackerRank Test
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val   # value of current node
        self.next = next # pointer to the next node

# Helper functions
"""
def build_linked_list(values):
    ""Convert Python list to Linked List""
    dummy = ListNode(-1)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    ""Convert Linked List back to Python list for easy output""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
"""

def mergeTwoLists(list1, list2):
    """Merge two sorted linked lists"""
    dummy = ListNode(-1)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 if list1 else list2
    return dummy.next

# Example test cases
if __name__ == "__main__":
    # Edge case 1: both lists empty
    l1 = build_linked_list([])
    l2 = build_linked_list([])
    print(linked_list_to_list(mergeTwoLists(l1, l2)))  # []

    # Edge case 2: one list empty
    l1 = build_linked_list([])
    l2 = build_linked_list([0])
    print(linked_list_to_list(mergeTwoLists(l1, l2)))  # [0]

    # Normal case
    l1 = build_linked_list([1,2,4])
    l2 = build_linked_list([1,3,4])
    print(linked_list_to_list(mergeTwoLists(l1, l2)))  # [1,1,2,3,4,4]