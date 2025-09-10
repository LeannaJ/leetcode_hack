# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        # Get grid dimensions
        rows = len(grid)                         # number of rows
        cols = len(grid[0]) if rows else 0      # number of cols (0 if empty)
        
        # Queue for BFS: store (r, c)
        q = deque()                              # positions of currently rotten oranges
        fresh = 0                                # count of fresh oranges
        
        # Initialize queue with all rotten oranges and count fresh ones
        for r in range(rows):                    # iterate over each row
            for c in range(cols):                # iterate over each column
                if grid[r][c] == 2:              # rotten orange
                    q.append((r, c))             # enqueue all initially rotten
                elif grid[r][c] == 1:            # fresh orange
                    fresh += 1                   # count fresh
            
        # If there are no fresh oranges, 0 minutes needed
        if fresh == 0:                           # already done
            return 0
        
        minutes = -1                             # will increment at each BFS level
        directions = [(1,0),(-1,0),(0,1),(0,-1)] # 4-directional movement
        
        # Multi-source BFS
        while q:                                 # while there are rotten sources to expand
            level_size = len(q)                  # number of nodes in the current minute
            minutes += 1                         # one minute passes per level
            for _ in range(level_size):          # process all nodes for this minute
                r, c = q.popleft()               # pop current rotten position
                for dr, dc in directions:        # explore 4 neighbors
                    nr, nc = r + dr, c + dc      # neighbor coordinates
                    # valid fresh neighbor turns rotten
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2         # mark as rotten
                        fresh -= 1               # decrease fresh count
                        q.append((nr, nc))       # enqueue for next minute
        
        # If all fresh became rotten, return minutes; else impossible -> -1
        return minutes if fresh == 0 else -1     # -1 means unreachable fresh oranges exist


# CoderPad/HackerRank Test
from collections import deque

def orangesRotting(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    
    # Initialize queue and fresh count
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    
    if fresh == 0:
        return 0
    
    minutes = -1
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    # Multi-source BFS
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    
    return minutes if fresh == 0 else -1


# Sample tests for CoderPad
if __name__ == "__main__":
    grids = [
        ([[2,1,1],[1,1,0],[0,1,1]], 4),   # all fresh can rot in 4 minutes
        ([[2,1,1],[0,1,1],[1,0,1]], -1),  # isolated fresh, impossible
        ([[0,2]], 0),                      # no fresh orange
        ([[1]], -1),                       # one fresh, no rotten
        ([], 0),                           # empty grid
    ]
    
    for grid, expected in grids:
        result = orangesRotting([row[:] for row in grid])  # copy grid to avoid mutation
        print(f"grid={grid} -> result={result} (expected={expected})")