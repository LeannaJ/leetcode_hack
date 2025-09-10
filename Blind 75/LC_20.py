# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # create a dummy node to simplify edge cases (empty result head handling)
        dummy = ListNode(-1)  # sentinel value; any value works
        # tail points to the last node in the merged list
        tail = dummy

        # p1 and p2 traverse list1 and list2 respectively
        p1, p2 = list1, list2

        # iterate while both lists have nodes
        while p1 and p2:
            # compare current values to maintain non-decreasing order
            if p1.val <= p2.val:
                # link p1 to the merged list
                tail.next = p1
                # advance p1
                p1 = p1.next
            else:
                # link p2 to the merged list
                tail.next = p2
                # advance p2
                p2 = p2.next
            # move tail forward to the newly added node
            tail = tail.next

        # at least one list is now exhausted; connect the remaining nodes
        tail.next = p1 if p1 else p2

        # the merged list starts at dummy.next
        return dummy.next


# CoderPad/HackerRank Test
# Singly linked list node definition
class ListNode:
    def __init__(self, val=0, next=None):
        # store the value
        self.val = val
        # pointer to the next node
        self.next = next

def merge_two_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merge two non-decreasing singly linked lists into one sorted list.
    Reuses existing nodes (O(1) extra space).
    """
    # dummy head to simplify head handling
    dummy = ListNode()
    # tail points to the end of the merged list
    tail = dummy

    # pointers for traversal
    p1, p2 = list1, list2

    # iterate while both lists have remaining nodes
    while p1 and p2:
        # choose the smaller (or equal) node to maintain stability
        if p1.val <= p2.val:
            # attach p1 to merged list
            tail.next = p1
            # move p1 forward
            p1 = p1.next
        else:
            # attach p2 to merged list
            tail.next = p2
            # move p2 forward
            p2 = p2.next
        # advance the tail pointer
        tail = tail.next

    # attach the remaining tail in one shot (if any)
    tail.next = p1 if p1 else p2

    # return the start of merged list (skip dummy)
    return dummy.next

# ---------- Helpers for CoderPad manual testing ----------
def build_list(iterable):
    # build a linked list from an iterable of values; returns head
    dummy = ListNode()
    cur = dummy
    for x in iterable:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def to_list(head):
    # convert linked list to Python list for quick assertions/prints
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

def is_non_decreasing(head):
    # sanity check: input is sorted (optional for interviews)
    cur = head
    while cur and cur.next:
        if cur.val > cur.next.val:
            return False
        cur = cur.next
    return True

if __name__ == "__main__":
    # ---- Edge cases to consider (quick sanity tests) ----
    # 1) one or both lists empty
    a1 = build_list([])
    b1 = build_list([1, 3, 5])
    merged1 = merge_two_sorted_lists(a1, b1)
    assert to_list(merged1) == [1, 3, 5]

    # 2) duplicates across lists
    a2 = build_list([1, 2, 4])
    b2 = build_list([1, 1, 3, 4])
    merged2 = merge_two_sorted_lists(a2, b2)
    assert to_list(merged2) == [1, 1, 1, 2, 3, 4, 4]

    # 3) single-element lists
    a3 = build_list([2])
    b3 = build_list([1])
    merged3 = merge_two_sorted_lists(a3, b3)
    assert to_list(merged3) == [1, 2]

    # 4) already one list entirely smaller
    a4 = build_list([1, 2, 3])
    b4 = build_list([10, 20])
    merged4 = merge_two_sorted_lists(a4, b4)
    assert to_list(merged4) == [1, 2, 3, 10, 20]

    # 5) large equal values
    a5 = build_list([5, 5, 5])
    b5 = build_list([5, 5])
    merged5 = merge_two_sorted_lists(a5, b5)
    assert to_list(merged5) == [5, 5, 5, 5, 5]

    # Optional: validate inputs are non-decreasing (comment out in real submissions if not required)
    assert is_non_decreasing(build_list([0, 0, 1]))
    # print(to_list(merged2))  # quick visual check
    print("All sample edge cases passed.")