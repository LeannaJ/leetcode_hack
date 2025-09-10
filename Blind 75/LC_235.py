# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Type 1
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Ensure p_val <= q_val to simplify comparisons
        # (not required, but makes the thinking straightforward)
        p_val = p.val  # store value of p
        q_val = q.val  # store value of q
        if p_val > q_val:  # swap so p_val is the smaller
            p_val, q_val = q_val, p_val

        cur = root  # start from the root
        while cur:  # traverse until we find the split point
            # If both targets are less than current, go left
            if q_val < cur.val:
                cur = cur.left
            # If both targets are greater than current, go right
            elif p_val > cur.val:
                cur = cur.right
            else:
                # Split point found: p <= cur <= q → cur is LCA
                return cur

        # In well-formed inputs (per problem), we never get here.
        return None

# Type 2
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Put smaller in a, larger in b for clean comparisons
        a, b = (p, q) if p.val <= q.val else (q, p)

        # Base case: if root is None, nothing to do (shouldn't happen per constraints)
        if not root:
            return None

        # If both targets are on the left side
        if b.val < root.val:
            return self.lowestCommonAncestor(root.left, a, b)

        # If both targets are on the right side
        if a.val > root.val:
            return self.lowestCommonAncestor(root.right, a, b)

        # Otherwise root is between a and b (or equals one of them) → LCA
        return root


# CoderPad/HackerRank Test
class TreeNode:
    def __init__(self, x: int):
        self.val = x          # node value
        self.left = None      # left child
        self.right = None     # right child

def lca_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find LCA of p and q in a BST iteratively.
    """
    # Ensure p_val <= q_val for clean comparisons
    p_val, q_val = (p.val, q.val) if p.val <= q.val else (q.val, p.val)

    cur = root  # start from the root
    while cur:  # walk down following BST property
        # Both targets lie in the left subtree
        if q_val < cur.val:
            cur = cur.left
        # Both targets lie in the right subtree
        elif p_val > cur.val:
            cur = cur.right
        else:
            # Split point (or equal to one target) found
            return cur

    # If not found (e.g., invalid input), return None
    return None

# Helper functions for testing
def insert_bst(root: TreeNode, val: int) -> TreeNode:
    """Insert a value into BST and return root."""
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def build_bst(values: list[int]) -> TreeNode:
    """Build BST from a list of values."""
    root = None
    for v in values:
        root = insert_bst(root, v)
    return root

def find_node(root: TreeNode, val: int) -> TreeNode:
    """Find node with given value in BST."""
    cur = root
    while cur:
        if cur.val == val:
            return cur
        elif val < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    return None


# --- Quick test cases ---
if __name__ == "__main__":
    # Build BST: [6,2,8,0,4,7,9,3,5]
    values = [6, 2, 8, 0, 4, 7, 9, 3, 5]
    root = build_bst(values)

    # Example 1: LCA of 2 and 8 is 6
    p = find_node(root, 2)
    q = find_node(root, 8)
    print("LCA of 2 and 8:", lca_bst(root, p, q).val)  # expected 6

    # Example 2: LCA of 2 and 4 is 2
    p = find_node(root, 2)
    q = find_node(root, 4)
    print("LCA of 2 and 4:", lca_bst(root, p, q).val)  # expected 2

    # Example 3: LCA of 3 and 5 is 4
    p = find_node(root, 3)
    q = find_node(root, 5)
    print("LCA of 3 and 5:", lca_bst(root, p, q).val)  # expected 4


# Enhanced Version - Robust version with edge-case handling
class TreeNode:
    def __init__(self, x: int):
        self.val = x          # node value
        self.left = None      # left child
        self.right = None     # right child

def bst_search(root: TreeNode, target: int) -> bool:
    """
    Return True if a node with value `target` exists in BST rooted at `root`.
    """
    cur = root                          # start from root
    while cur:                          # traverse until None
        if target == cur.val:           # found the value
            return True
        elif target < cur.val:          # search left
            cur = cur.left
        else:                           # search right
            cur = cur.right
    return False                        # not found

def lca_bst_safe(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """
    LCA in BST with input validation:
    - Returns None if root is None or if either p or q is None
      or if either p or q does not exist in the tree.
    - Handles case where p == q (then that node is the LCA).
    """
    # Basic null checks
    if root is None or p is None or q is None:  # invalid input
        return None

    # Optional: verify both p and q exist in the tree
    if not bst_search(root, p.val) or not bst_search(root, q.val):
        return None  # one or both nodes are not in this BST

    # If both references are actually the same tree node (or same value in a unique-BST assumption)
    if p.val == q.val:
        # In a unique-key BST, the LCA is that node itself
        return p

    # Normalize so p_val <= q_val
    p_val, q_val = (p.val, q.val) if p.val <= q.val else (q.val, p.val)

    cur = root  # start traversal
    while cur:
        # If both lie left
        if q_val < cur.val:
            cur = cur.left
        # If both lie right
        elif p_val > cur.val:
            cur = cur.right
        else:
            # Split point (or equals one) is the LCA
            return cur

    # Should not happen if inputs verified; return None for completeness
    return None