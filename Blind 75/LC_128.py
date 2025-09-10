# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums):
        # Handle empty input quickly
        if not nums:
            return 0  # No elements => longest length is 0

        # Put all numbers into a hash set for O(1) average lookups
        num_set = set(nums)  # Removes duplicates as well

        # Track the best (maximum) sequence length found
        best = 0  # Will store the maximum length of any consecutive sequence

        # Iterate through the original list (or set; list is fine)
        for x in num_set:  # Iterate unique values only
            # Only start counting if 'x' is the start of a sequence
            # A start means (x - 1) is NOT present in the set
            if (x - 1) not in num_set:
                # 'x' is the start; expand forward
                cur = x              # Current number to check
                length = 1           # Current sequence length (at least x itself)

                # Keep extending while the next consecutive number exists
                while (cur + 1) in num_set:
                    cur += 1         # Move to next number
                    length += 1      # Increase sequence length

                # Update global best if this sequence is longer
                if length > best:
                    best = length    # Record new maximum

        # Return the maximum length found
        return best


# CoderPad/HackerRank Test
from typing import List

def longest_consecutive(nums: List[int]) -> int:
    """
    Return the length of the longest consecutive elements sequence.
    Average time: O(n), space: O(n).
    """
    # Use a set for O(1) average membership and unique values
    s = set(nums)      # deduplicate
    best = 0           # track longest length
    
    # Iterate each unique number and only start at sequence starts
    for x in s:
        # Start if there is no predecessor for x
        if (x - 1) not in s:
            cur = x
            length = 1
            
            # Expand to the right while consecutive numbers exist
            while (cur + 1) in s:
                cur += 1
                length += 1
            
            # Update the global best
            if length > best:
                best = length
    
    return best

# Example quick tests (can delete in interview)
# You can comment this out if interviewer prefers to run their own tests.
if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))           # 4
    print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))            # 9
    print(longest_consecutive([-3, -2, -1, 10]))                 # 3
    print(longest_consecutive([1,1,1]))                          # 1
    print(longest_consecutive([]))                               # 0


# If stdin is provided
from typing import List

def longest_consecutive(nums: List[int]) -> int:
    # Same core logic as above
    s = set(nums)
    best = 0
    for x in s:
        if (x - 1) not in s:
            cur = x
            length = 1
            while (cur + 1) in s:
                cur += 1
                length += 1
            if length > best:
                best = length
    return best

if __name__ == "__main__":
    # Example spec:
    # line1: n
    # line2: n integers
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    # Optional: trim to n if extra tokens are present
    arr = arr[:n]
    print(longest_consecutive(arr))