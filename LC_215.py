# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Type 1
# Time: Average O(n), Worst O(n^2); Space: O(1) extra (in-place)

import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Convert kth largest to (n-k)th smallest index
        # e.g., largest -> index n-1, kth largest -> index n-k
        target = len(nums) - k  # target index in sorted ascending order

        # Quickselect helper to position the pivot at its final sorted index
        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot_value = nums[pivot_index]            # choose pivot value
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # move pivot to end
            store_index = left                         # store index for smaller elements
            for i in range(left, right):               # iterate through subarray
                if nums[i] < pivot_value:              # if element < pivot
                    nums[store_index], nums[i] = nums[i], nums[store_index]  # swap to the left part
                    store_index += 1                   # advance store index
            nums[right], nums[store_index] = nums[store_index], nums[right]  # move pivot to its final place
            return store_index                         # final pivot position

        left, right = 0, len(nums) - 1                 # search boundaries
        while True:                                    # loop until we return
            pivot_index = random.randint(left, right)  # randomize pivot to avoid worst case
            pivot_index = partition(left, right, pivot_index)  # partition around pivot
            if pivot_index == target:                  # found the target index
                return nums[pivot_index]              # return the kth largest
            elif pivot_index < target:                 # target on the right side
                left = pivot_index + 1                 # move left bound
            else:                                      # target on the left side
                right = pivot_index - 1                # move right bound


# Type 2
# Time: O(n log k); Space: O(k)

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap: list[int] = []               # create an empty min-heap
        for x in nums:                         # iterate all numbers
            if len(min_heap) < k:              # if heap size is less than k
                heapq.heappush(min_heap, x)    # push current element
            else:
                if x > min_heap[0]:            # if current element is larger than heap min
                    heapq.heapreplace(min_heap, x)  # pop min and push x in one step
        return min_heap[0]                     # root is kth largest after processing


# CoderPad/HackerRank Test

import random

def kth_largest(nums: list[int], k: int) -> int:
    # Convert kth largest to (n-k)th smallest index
    target = len(nums) - k

    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_value = nums[pivot_index]                          # pick pivot value
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # move pivot to end
        store = left                                             # boundary for < pivot
        for i in range(left, right):                             # scan subarray
            if nums[i] < pivot_value:                            # place smaller values to the left
                nums[store], nums[i] = nums[i], nums[store]      # swap
                store += 1                                       # advance boundary
        nums[store], nums[right] = nums[right], nums[store]      # place pivot in final spot
        return store                                             # return pivot's final index

    left, right = 0, len(nums) - 1                               # search boundaries
    while True:                                                  # iterative quickselect
        pivot = random.randint(left, right)                      # random pivot
        p = partition(left, right, pivot)                        # partition
        if p == target:                                          # found target index
            return nums[p]                                       # return answer
        elif p < target:                                         # search right part
            left = p + 1
        else:                                                    # search left part
            right = p - 1

# Simple ad-hoc tests (comment out if platform provides its own tests)
if __name__ == "__main__":
    print(kth_largest([3,2,1,5,6,4], 2))   # 5
    print(kth_largest([3,2,3,1,2,4,5,5,6], 4))  # 4


# Enhanced Version - Robust version with edge-case handling
import random
from typing import Iterable

def kth_largest_safe(nums: Iterable[int], k: int, *, seed: int | None = None, debug: bool = False) -> int:
    # Convert to list to allow in-place partitioning; also validates iterables
    arr = list(nums)                                            # materialize iterable
    n = len(arr)                                                # length

    # Basic validations with clear error messages
    if n == 0:                                                  # empty input
        raise ValueError("nums must be non-empty")
    if not isinstance(k, int):                                  # k type check
        raise TypeError("k must be an integer")
    if not (1 <= k <= n):                                       # k range check
        raise ValueError(f"k must be in [1, {n}]")

    # Optional deterministic randomness for reproducibility
    rng = random.Random(seed) if seed is not None else random   # choose RNG

    target = n - k                                              # (n-k)th smallest index

    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_value = arr[pivot_index]                          # pivot value
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # move pivot to end
        store = left                                            # boundary for < pivot
        for i in range(left, right):                            # scan window
            if arr[i] < pivot_value:                            # smaller goes left
                arr[store], arr[i] = arr[i], arr[store]         # swap
                store += 1                                      # advance boundary
        arr[store], arr[right] = arr[right], arr[store]         # pivot to final spot
        if debug:                                               # optional trace
            print(f"[partition] left={left} right={right} pivot={pivot_value} -> idx={store}")
        return store                                            # final pivot index

    left, right = 0, n - 1                                      # bounds
    while True:                                                 # loop until return
        pivot = rng.randint(left, right)                        # randomized pivot
        p = partition(left, right, pivot)                       # partition around pivot
        if p == target:                                         # found index
            return arr[p]                                       # return kth largest
        elif p < target:                                        # go right
            left = p + 1
        else:                                                   # go left
            right = p - 1

# Example usage / sanity checks
if __name__ == "__main__":
    print(kth_largest_safe([3,2,1,5,6,4], 2))                 # 5
    print(kth_largest_safe([3,2,3,1,2,4,5,5,6], 4, debug=True)) # 4 + trace
    # Edge cases:
    # print(kth_largest_safe([], 1))                           # raises ValueError
    # print(kth_largest_safe([1,2], 3))                        # raises ValueError