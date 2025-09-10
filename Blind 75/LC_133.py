# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Dictionary to map original node -> cloned node
        old_to_new = {}

        # DFS function
        def dfs(curr):
            # If node is None, return None
            if not curr:
                return None

            # If we already cloned this node, return the cloned version
            if curr in old_to_new:
                return old_to_new[curr]

            # Clone the current node (without neighbors for now)
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # Recursively clone the neighbors
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)


# CoderPad/HackerRank Test
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    # Edge case: if the graph is empty
    if not node:
        return None

    # Dictionary to map original node -> cloned node
    old_to_new = {}
    
    # Create the clone for the starting node
    old_to_new[node] = Node(node.val)
    
    # BFS queue
    queue = deque([node])
    
    while queue:
        curr = queue.popleft()
        
        for nei in curr.neighbors:
            if nei not in old_to_new:
                # Clone the neighbor if not already cloned
                old_to_new[nei] = Node(nei.val)
                queue.append(nei)
            
            # Add the cloned neighbor to the cloned current node
            old_to_new[curr].neighbors.append(old_to_new[nei])
    
    return old_to_new[node]

# Example execution (Optional)
if __name__ == "__main__":
    # Build a tiny graph: 1 -- 2
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors = [node2]
    node2.neighbors = [node1]

    clone = cloneGraph(node1)
    print(clone.val)                # 1
    print([n.val for n in clone.neighbors])  # 2