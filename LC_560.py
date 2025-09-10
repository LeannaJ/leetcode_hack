# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count_map tracks how many times a prefix sum has appeared
        count_map = defaultdict(int)   # key: prefix sum, value: frequency
        count_map[0] = 1               # to count subarrays that start at index 0
        
        cur = 0                        # running prefix sum
        ans = 0                        # total count of subarrays summing to k
        
        for x in nums:
            cur += x                   # update running sum
            need = cur - k             # we want previous prefix == cur - k
            ans += count_map[need]     # add how many times 'need' appeared
            count_map[cur] += 1        # record current prefix sum
        return ans


# CoderPad/HackerRank Test
from collections import defaultdict
from typing import List

def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    Return the number of continuous subarrays whose sum equals k.
    Uses prefix-sum + hashmap in O(n) time and O(n) space.
    """
    # Edge case: empty list -> zero subarrays
    if not nums:
        return 0

    # count_map[prefix] = number of times this prefix sum has appeared
    count_map = defaultdict(int)
    count_map[0] = 1  # counts subarrays starting at index 0 that sum to k

    cur = 0   # running prefix sum
    ans = 0   # answer accumulator

    for val in nums:
        cur += val                           # update running sum
        need = cur - k                       # we need a previous prefix 'need'
        ans += count_map.get(need, 0)        # add how many times 'need' occurred
        count_map[cur] += 1                  # record current prefix sum
    return ans


# --- Minimal sanity tests (non-exhaustive) ---
if __name__ == "__main__":
    # Typical case
    print(subarray_sum_equals_k([1,1,1], 2))        # expected 2

    # Includes negatives (sliding window would fail; hashmap works)
    print(subarray_sum_equals_k([1,2,3,-2,5,-3,1], 3))  # expected 5

    # Single element equals k
    print(subarray_sum_equals_k([3], 3))            # expected 1

    # No subarray sums to k
    print(subarray_sum_equals_k([2,4,6], 5))        # expected 0

    # Zeros and multiple overlapping subarrays
    print(subarray_sum_equals_k([0,0,0], 0))        # expected 6
    # Explanation: all subarrays count when k=0: C(3,1)+C(3,2)+C(3,3)=3+3+1=7? Careful.
    # Actually contiguous subarrays:
    # [0](i=0), [0](i=1), [0](i=2), [0,0](0..1), [0,0](1..2), [0,0,0](0..2) => 6

    # Empty input edge case
    print(subarray_sum_equals_k([], 0))             # expected 0
        