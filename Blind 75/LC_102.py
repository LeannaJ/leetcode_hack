# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # store the node value
        self.val = val
        # pointer to left child
        self.left = left
        # pointer to right child
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root):
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        # Initialize a queue for BFS with the root node
        queue = deque([root])
        # This will store the final level order traversal
        result = []
        
        # Continue until there are no more nodes to process
        while queue:
            # Number of nodes in the current level
            level_size = len(queue)
            # List to collect values for this level
            level_vals = []
            
            # Process exactly 'level_size' nodes (one full level)
            for _ in range(level_size):
                # Pop from the left of the queue (FIFO)
                node = queue.popleft()
                # Record the current node's value
                level_vals.append(node.val)
                # Push left child if it exists
                if node.left:
                    queue.append(node.left)
                # Push right child if it exists
                if node.right:
                    queue.append(node.right)
            
            # After processing the level, append collected values
            result.append(level_vals)
        
        # Return the level order traversal
        return result


# CoderPad/HackerRank Test
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_vals = []
        for _ in range(level_size):
            node = queue.popleft()
            level_vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_vals)
    
    return result

# Example usage (for demonstration in CoderPad)
if __name__ == "__main__":
    root = TreeNode(3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(level_order(root))  # [[3], [9,20], [15,7]]