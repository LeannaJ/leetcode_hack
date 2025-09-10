# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Type 1
class Solution:
    def maxDepth(self, root):
        # If the current node is None, depth is 0
        if not root:
            return 0
        # Compute the max depth of left subtree
        left_depth = self.maxDepth(root.left)
        # Compute the max depth of right subtree
        right_depth = self.maxDepth(root.right)
        # Current node contributes +1 depth
        return 1 + max(left_depth, right_depth)

# Type 2
from collections import deque

class Solution:
    def maxDepth(self, root):
        # If the tree is empty, depth is 0
        if not root:
            return 0
        # Use a queue for level-order traversal
        q = deque([root])
        depth = 0
        # Process nodes level by level
        while q:
            # Each iteration processes one whole level
            for _ in range(len(q)):
                node = q.popleft()
                # Add children for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Completed one level
            depth += 1
        return depth


# CoderPad/HackerRank Test
from collections import deque

def maxDepth(root):
    # Edge case: empty tree
    if not root:
        return 0
    
    q = deque([root])  # queue for BFS
    depth = 0
    
    while q:
        # Process one level at a time
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1  # completed one level
    
    return depth

# --- Sample usage (for quick test in CoderPad) ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build a small tree:
#       3
#      / \
#     9  20
#        / \
#       15  7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(maxDepth(root))  # Expected output: 3
print(maxDepth(None))  # Expected output: 0 (empty tree)
print(maxDepth(TreeNode(1)))  # Expected output: 1 (single node)