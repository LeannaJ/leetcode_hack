# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Monotonic deque solution: O(n) time, O(k) space.
        """
        # Edge cases for LeetCode are typically well-formed, but we guard minimal cases
        if not nums or k == 0:
            return []
        if k == 1:
            # Each single-element window's max is the element itself
            return nums[:]

        dq = deque()  # will store indices, with nums[dq[0]] as the current window max
        res = []      # result list to collect window maxima

        for i, val in enumerate(nums):
            # 1) Maintain decreasing order in deque by value:
            # Pop from the right all indices whose value <= current val
            while dq and nums[dq[-1]] <= val:
                dq.pop()

            # 2) Push current index
            dq.append(i)

            # 3) Remove indices that are out of the current window (left boundary is i - k + 1)
            left = i - k + 1
            if dq[0] < left:
                dq.popleft()

            # 4) Record result once the first full window is formed
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


# CoderPad/HackerRank Test
from collections import deque
from typing import List, Optional

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    """
    Compute maximum in each sliding window of size k using a monotonic deque.
    Time: O(n), Space: O(k)
    """
    # --- Robust edge cases (important in live platforms) ---
    # If nums is None, treat as empty.
    if nums is None:
        return []
    # If k is invalid (<= 0), return empty as there is no valid window.
    if k <= 0:
        return []
    # If k == 1, each element is the window max.
    if k == 1:
        return nums[:]
    # If k > len(nums), by common conventions either:
    #   - return [] (no full window), or
    #   - return [max(nums)] once (treat one big window).
    # For interviews, clarify; here we return [] to match LC-style behavior.
    if k > len(nums):
        return []

    dq = deque()  # stores indices in decreasing order of their values
    res = []

    for i, val in enumerate(nums):
        # Remove smaller/equal values from the right to keep deque decreasing
        while dq and nums[dq[-1]] <= val:
            dq.pop()

        # Push current index
        dq.append(i)

        # Remove indices that are out of window from the left
        left = i - k + 1
        if dq[0] < left:
            dq.popleft()

        # Append max once we have the first full window
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res

# --- Minimal test harness for CoderPad/HackerRank ---
def run_demo():
    """
    Simple demo without external input parsing (adjust as needed).
    """
    # Basic cases
    print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))  # expected: [3,3,5,5,6,7]
    print(sliding_window_max([1], 1))                  # expected: [1]
    print(sliding_window_max([9, 8, 7, 6], 2))         # expected: [9,8,7]
    print(sliding_window_max([4,4,4,4], 2))            # expected: [4,4,4]
    print(sliding_window_max([], 3))                   # expected: []
    print(sliding_window_max([2,1], 3))                # k > n -> []
    print(sliding_window_max(None, 2))                 # None -> []
    print(sliding_window_max([1,2,3], 0))              # k <= 0 -> []

if __name__ == "__main__":
    # In a real interview, you might parse input here if required.
    run_demo()