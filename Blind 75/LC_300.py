# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

# Time: O(n log n), Space: O(n)
from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[k] holds the minimum possible tail of an increasing subsequence
        # with length k+1 found so far.
        tails = []  # will be sorted non-decreasingly
        
        for x in nums:
            # Find the first index in tails where x can fit (lower_bound)
            i = bisect_left(tails, x)  # O(log n)
            if i == len(tails):
                # x extends the longest subsequence found so far
                tails.append(x)
            else:
                # x could potentially start a better subsequence of length i+1
                tails[i] = x
        # The length of tails equals the length of the LIS
        return len(tails)


# CoderPad/HackerRank Test
# Time: O(n log n), Space: O(n)
from bisect import bisect_left
import sys

def length_of_lis(nums):
    # tails[k] = minimum possible tail of an increasing subsequence of length k+1
    tails = []
    for x in nums:
        i = bisect_left(tails, x)  # find first >= x to keep strictly increasing
        if i == len(tails):
            tails.append(x)        # extend LIS
        else:
            tails[i] = x           # improve existing length
    return len(tails)

def parse_ints_from_line(line: str):
    # Split by whitespace and parse ints; ignore non-int tokens gracefully
    out = []
    for tok in line.strip().split():
        try:
            out.append(int(tok))
        except ValueError:
            # skip tokens that are not integers (defensive in live settings)
            continue
    return out

def main():
    # Read entire stdin and merge tokens (supports multi-line paste)
    data = sys.stdin.read()
    nums = parse_ints_from_line(data)
    if not nums:
        # Edge case: empty input -> LIS length is 0
        print(0)
        return
    print(length_of_lis(nums))

if __name__ == "__main__":
    main()