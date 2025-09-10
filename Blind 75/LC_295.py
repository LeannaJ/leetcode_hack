# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:
    def __init__(self):
        # lower: max-heap simulated by storing negatives
        self.lower = []  # type: list[int]
        # upper: regular min-heap
        self.upper = []  # type: list[int]

    def addNum(self, num: int) -> None:
        # Step 1: push to lower (as negative to simulate max-heap)
        heapq.heappush(self.lower, -num)  # store negative to make max-heap behavior
        # Step 2: move the largest from lower to upper to maintain ordering invariant
        heapq.heappush(self.upper, -heapq.heappop(self.lower))  # ensure all in lower <= all in upper
        # Step 3: rebalance sizes so that len(lower) >= len(upper) and diff <= 1
        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))  # move one back to lower

    def findMedian(self) -> float:
        # If odd count: lower has one extra element
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])  # top of max-heap (negated back)
        # If even count: average the two middles
        return (-self.lower[0] + self.upper[0]) / 2.0  # average of two heap tops


# CoderPad/HackerRank Test
import heapq
from typing import Optional, Union

Number = Union[int, float]

class MedianFinder:
    def __init__(self) -> None:
        # lower half as a max-heap (store negatives)
        self.lower: list[Number] = []  # max-heap simulated via negatives
        # upper half as a min-heap
        self.upper: list[Number] = []  # min-heap

    def _rebalance(self) -> None:
        # keep sizes balanced: len(lower) >= len(upper) and size diff <= 1
        if len(self.upper) > len(self.lower):
            # move the smallest from upper to lower
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
        elif len(self.lower) - len(self.upper) > 1:
            # move the largest from lower to upper
            heapq.heappush(self.upper, -heapq.heappop(self.lower))

    def addNum(self, num: Number) -> None:
        # guard: silently ignore NaN-like or non-numeric (simple, interview-friendly)
        # In a stricter setting, raise TypeError instead.
        if not isinstance(num, (int, float)):
            return  # or: raise TypeError("num must be int or float")
        # insert into lower as negative to simulate max-heap
        heapq.heappush(self.lower, -num)  # push negative for max-heap behavior
        # ensure ordering: all elements in lower <= all in upper
        heapq.heappush(self.upper, -heapq.heappop(self.lower))  # move largest of lower into upper
        # rebalance sizes
        self._rebalance()

    def findMedian(self) -> float:
        # raises a clear error if called on empty stream (explicit edge-case handling)
        if not self.lower and not self.upper:
            raise ValueError("No elements have been added; median is undefined.")
        # odd count
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        # even count
        return (-self.lower[0] + self.upper[0]) / 2.0

    # optional: safe variant for platforms/tests that prefer None over exceptions
    def try_find_median(self) -> Optional[float]:
        # return None if no numbers yet, else median
        if not self.lower and not self.upper:
            return None
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2.0

if __name__ == "__main__":
    # Minimal demo (commented out to avoid I/O during tests):
    # mf = MedianFinder()
    # for x in [5, 15, 1, 3]:
    #     mf.addNum(x)
    #     print("median:", mf.findMedian())
    pass
        