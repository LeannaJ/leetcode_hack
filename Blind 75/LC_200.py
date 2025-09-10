# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Handle empty grid
        if not grid or not grid[0]:
            return 0
        
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        
        # Define DFS to sink connected land
        def dfs(r: int, c: int) -> None:
            # Boundary and water checks
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            # Mark current land as visited by sinking it to '0'
            grid[r][c] = '0'
            # Explore 4-directionally
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Count islands
        count = 0
        for r in range(rows):
            for c in range(cols):
                # Start DFS whenever a new island cell is found
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count


# CoderPad/HackerRank Test
# Function-only style for live coding platforms
# Time: O(R*C), Space: O(R*C) worst-case
from collections import deque

def num_islands(grid):
    """
    Count islands (groups of '1's) in a 2D grid using BFS to avoid recursion depth issues.
    """
    # Guard for empty input
    if not grid or not grid[0]:
        return 0
    
    # Dimensions
    rows, cols = len(grid), len(grid[0])
    # Directions: up, down, left, right
    DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
    # Local copy not required—mutate grid in-place to mark visited
    count = 0
    
    # Iterate over all cells
    for r in range(rows):
        for c in range(cols):
            # If land is found, start BFS and increment island count
            if grid[r][c] == '1':
                count += 1
                # Use queue for BFS
                q = deque()
                q.append((r, c))
                # Mark as visited by sinking to '0'
                grid[r][c] = '0'
                
                # Standard BFS
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in DIRS:
                        nr, nc = cr + dr, cc + dc
                        # Check bounds and unvisited land
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'  # mark visited
                            q.append((nr, nc))
    return count

# --- minimal sanity check ---
if __name__ == "__main__":
    g = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"],
    ]
    print(num_islands(g))  # 1
        