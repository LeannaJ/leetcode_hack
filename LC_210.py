# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list and indegree array
        # graph[b] contains a list of courses that depend on course b
        graph = defaultdict(list)                           # adjacency list
        indeg = [0] * numCourses                            # indegree for each course
        
        # Fill graph and indegree from prerequisites
        for a, b in prerequisites:
            graph[b].append(a)                              # edge: b -> a (must take b before a)
            indeg[a] += 1                                   # a has one more prerequisite
        
        # Initialize queue with all courses that have no prerequisites
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        
        order = []                                          # resulting topological order
        
        # Process courses with BFS
        while q:
            cur = q.popleft()                               # take a course with indegree 0
            order.append(cur)                               # add to order
            
            for nxt in graph[cur]:                          # for each course depending on cur
                indeg[nxt] -= 1                             # we've satisfied one prereq
                if indeg[nxt] == 0:                         # if no more prereqs
                    q.append(nxt)                           # it's ready to be taken
        
        # If we placed all courses, return the order; otherwise, cycle exists
        return order if len(order) == numCourses else []


# CoderPad/HackerRank Test
from collections import deque, defaultdict
from typing import List, Iterable, Tuple, Set

def find_order(num_courses: int, prerequisites: Iterable[Tuple[int, int]]) -> List[int]:
    """
    Return a valid order to take all courses or [] if impossible.
    BFS (Kahn's algorithm) with light input validation and deduplication.
    """
    # Guard: invalid course count
    if num_courses <= 0:
        return []
    
    # Deduplicate edges and filter invalid pairs
    edges: Set[Tuple[int, int]] = set()  # store unique (a,b)
    for pair in prerequisites:
        # Basic structural validation
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            continue  # skip malformed entries gracefully in interview
        a, b = pair
        # Out-of-range nodes are ignored to keep function total
        if not (0 <= a < num_courses and 0 <= b < num_courses):
            continue
        # Self-dependency means impossible immediately
        if a == b:
            return []
        edges.add((a, b))  # dedup
    
    # Build graph and indegree
    graph = defaultdict(list)                # b -> [a1, a2, ...]
    indeg = [0] * num_courses
    for a, b in edges:
        graph[b].append(a)
        indeg[a] += 1
    
    # Queue init with zero indegree
    q = deque([i for i in range(num_courses) if indeg[i] == 0])
    order: List[int] = []
    
    # Kahn's algorithm
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    # If not all placed, cycle exists
    return order if len(order) == num_courses else []

# --- minimal demonstration (you can comment out in real interview) ---
if __name__ == "__main__":
    # Example 1: possible
    print(find_order(4, [(1,0),(2,0),(3,1),(3,2)]))  # one valid: [0,1,2,3] or [0,2,1,3]
    # Example 2: cycle
    print(find_order(2, [(0,1),(1,0)]))              # []
    # Edge: self dependency
    print(find_order(2, [(1,1)]))                    # []
    # Edge: duplicate edges
    print(find_order(2, [(1,0),(1,0),(1,0)]))        # [0,1]
    # Edge: out-of-range pair ignored
    print(find_order(2, [(1,0),(2,0)]))              # [0,1]