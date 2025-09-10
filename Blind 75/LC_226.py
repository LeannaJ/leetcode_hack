# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):
        # Base case: if the node is None, nothing to invert
        if root is None:
            return None
        
        # Recursively invert left and right subtrees
        left_inverted = self.invertTree(root.left)    # invert the left subtree
        right_inverted = self.invertTree(root.right)  # invert the right subtree
        
        # Swap the children
        root.left, root.right = right_inverted, left_inverted
        
        # Return the current root after inversion
        return root


# CoderPad/HackerRank Test
from collections import deque
from typing import Optional

class TreeNode:
    # Basic binary tree node
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Empty tree: nothing to invert
    if root is None:
        return None

    # Use BFS to avoid recursion depth issues on skewed trees
    q = deque([root])                         # queue for level-order traversal
    while q:
        node = q.popleft()                    # take current node
        node.left, node.right = node.right, node.left  # swap children in-place
        if node.left:                         # enqueue left if exists
            q.append(node.left)
        if node.right:                        # enqueue right if exists
            q.append(node.right)
    return root

# Helper functions
def build_tree(level: List[Optional[Any]]) -> Optional[TreeNode]:
    if not level or level[0] is None: return None
    it = iter(level[1:])
    root = TreeNode(level[0])
    q = deque([root])
    for l, r in zip(it, it):
        node = q.popleft()
        if l is not None:
            node.left = TreeNode(l); q.append(node.left)
        if r is not None:
            node.right = TreeNode(r); q.append(node.right)
    return root

def serialize(root: Optional[TreeNode]) -> List[Optional[Any]]:
    if not root: return []
    out, q = [], deque([root])
    while q:
        n = q.popleft()
        if n:
            out.append(n.val); q.append(n.left); q.append(n.right)
        else:
            out.append(None)
    while out and out[-1] is None: out.pop()
    return out

# Example usage (for demonstration in CoderPad)
if __name__ == "__main__":
    root = build_tree([4,2,7,1,3,6,9])
    print(serialize(invert_tree(root)))  # [4,7,2,9,6,3,1]