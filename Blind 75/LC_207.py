# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

from collections import deque, defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list and in-degree array
        graph = defaultdict(list)           # adjacency list: pre -> [next courses]
        indegree = [0] * numCourses         # indegree[i] = number of prerequisites for course i
        
        # Populate graph and indegree
        for nxt, pre in prerequisites:      # each pair means: pre -> nxt (nxt depends on pre)
            graph[pre].append(nxt)          # add edge pre -> nxt
            indegree[nxt] += 1              # nxt has one more incoming edge
        
        # Initialize queue with courses that have no prerequisites
        q = deque([c for c in range(numCourses) if indegree[c] == 0])  # all roots
        
        taken = 0                           # count how many courses we can take
        while q:                            # BFS over DAG layers
            cur = q.popleft()               # take a course whose prerequisites satisfied
            taken += 1                      # one more course is completed
            for nxt in graph[cur]:          # reduce indegree of neighbors
                indegree[nxt] -= 1          # we "used up" cur as a prerequisite
                if indegree[nxt] == 0:      # if neighbor now has no remaining prereqs
                    q.append(nxt)           # it's ready to be taken
        
        # If we took all courses, there was no cycle; otherwise, cycle exists
        return taken == numCourses          # True if no cycle, False if cycle


# CoderPad/HackerRank Test
from collections import deque, defaultdict
from typing import List, Tuple

def can_finish(num_courses: int, prerequisites: List[Tuple[int, int]]) -> bool:
    # Guard: invalid course count
    if num_courses < 0:                     # negative course count is invalid
        return False                        # decide False (cannot schedule)
    if num_courses == 0:                    # zero courses => trivially finishable
        return True

    graph = defaultdict(list)               # adjacency list: pre -> [nxt]
    indegree = [0] * num_courses            # indegree per course

    seen_edges = set()                      # to ignore exact duplicates like (a,b) repeated

    for nxt, pre in prerequisites:          # each is (nxt, pre): pre -> nxt
        # Guard: out-of-range indices
        if not (0 <= nxt < num_courses) or not (0 <= pre < num_courses):
            return False                    # invalid input — treat as not finishable

        # Guard: self-dependency implies immediate cycle
        if nxt == pre:
            return False

        # Deduplicate identical edges to avoid inflating indegree
        if (nxt, pre) in seen_edges:        # skip duplicate edges
            continue
        seen_edges.add((nxt, pre))

        graph[pre].append(nxt)              # add directed edge
        indegree[nxt] += 1                  # track prerequisites count

    # Start with all zero-indegree nodes
    q = deque(i for i in range(num_courses) if indegree[i] == 0)

    taken = 0                               # number of courses we can complete
    while q:                                # Kahn's algorithm BFS
        cur = q.popleft()                   # pop a ready course
        taken += 1                          # we "take" it
        for nxt in graph[cur]:              # relax outgoing edges
            indegree[nxt] -= 1              # one prerequisite satisfied
            if indegree[nxt] == 0:          # if now unlocked
                q.append(nxt)               # enqueue

    return taken == num_courses             # True iff no cycle

# Minimal runnable harness for CoderPad/HackerRank manual tests
if __name__ == "__main__":
    # Example 1: can finish (no cycle)
    print(can_finish(2, [(1, 0)]))          # True

    # Example 2: cannot finish (cycle 0->1->0)
    print(can_finish(2, [(1, 0), (0, 1)]))  # False

    # Edge: n=0
    print(can_finish(0, []))                # True

    # Edge: self-loop
    print(can_finish(1, [(0, 0)]))          # False

    # Edge: out-of-range
    print(can_finish(2, [(2, 0)]))          # False

    # Edge: duplicates (should not overcount)
    print(can_finish(3, [(1, 0), (1, 0), (2, 1)]))  # True