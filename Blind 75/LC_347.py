# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies of each number
        freq = defaultdict(int)                     # map: number -> count
        for x in nums:
            freq[x] += 1                            # increment count
        
        # Step 2: Build buckets where index = frequency
        # Max frequency can't exceed len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]  # each bucket holds numbers
        for num, count in freq.items():
            buckets[count].append(num)              # put number into its frequency bucket
        
        # Step 3: Gather results from highest frequency down
        res = []                                     # will store top-k frequent numbers
        for f in range(len(buckets) - 1, 0, -1):     # iterate from highest freq to 1
            if buckets[f]:                           # if there are numbers with freq f
                res.extend(buckets[f])               # add them to result
                if len(res) >= k:                    # stop once we have k elements
                    return res[:k]                   # trim in case we added extra
        
        return res[:k]                               # fallback (the loop should already return)


# CoderPad/HackerRank Test
from collections import defaultdict
from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # Edge case: empty input or non-positive k
    if not nums or k <= 0:
        return []  # nothing to return
    
    # Edge case: k >= unique count -> return all unique elements
    # (order doesn't matter for this problem)
    # Build frequency map first
    freq = defaultdict(int)                  # number -> frequency
    for x in nums:
        freq[x] += 1                         # count frequency
    
    if k >= len(freq):
        # Return any order of unique keys
        return list(freq.keys())
    
    # Bucket sort approach: index = frequency, value = list of numbers
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)
    
    # Collect from highest frequency down until we have k items
    result = []
    for f in range(len(buckets) - 1, 0, -1):
        if buckets[f]:
            result.extend(buckets[f])
            if len(result) >= k:
                return result[:k]
    
    # Fallback (should not reach here with valid k)
    return result[:k]

# Optional: if interviewer prefers heap:
"""
import heapq
from collections import Counter
def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    if not nums or k <= 0:
        return []
    
    counts = Counter(nums)
    if k >= len(counts):
        return list(counts.keys())
    heap = []

    for num, c in counts.items():
        heapq.heappush(heap, (c, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]
"""