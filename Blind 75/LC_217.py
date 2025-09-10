# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# Type 1
# Time: O(n), Space: O(n)
# Approach: Use a hash set to track seen numbers. If we see a number twice, return True.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         # Initialize an empty set to keep track of seen numbers
        seen = set()  # set of ints we've encountered
        
        # Iterate over each number in the array
        for x in nums:  # go through each element once
            # If x is already in the set, we found a duplicate
            if x in seen:  # membership check is average O(1)
                return True  # early exit as soon as a duplicate is found
            # Otherwise, record x as seen
            seen.add(x)  # add current number to the set
        
        # If we finish the loop without finding duplicates, return False
        return False  # no duplicates found

# Type 2
# Time: O(n log n), Space: O(1) extra (in-place sort) or O(n) depending on language/impl.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sort the array so duplicates (if any) become adjacent
        nums.sort()  # O(n log n)
        
        # Compare each element to its neighbor
        for i in range(1, len(nums)):  # scan once
            # If two adjacent values are equal, duplicate exists
            if nums[i] == nums[i - 1]:
                return True
        
        # If no adjacent equals were found, no duplicates
        return False


# CoderPad/HackerRank Test
def contains_duplicate(nums):
    # Use a set to remember what we've seen
    seen = set()  # holds unique numbers encountered so far
    
    for x in nums:  # iterate through all numbers once
        if x in seen:  # if x was seen before, we found a duplicate
            return True  # early return when duplicate detected
        seen.add(x)  # remember this number
    
    return False  # no duplicates found

# --- Minimal sanity checks ---
if __name__ == "__main__":
    print(contains_duplicate([1,2,3,1]))  # True
    print(contains_duplicate([1,2,3,4]))  # False
    print(contains_duplicate([]))         # False


# Enhanced Version - Robust version with edge-case handling
def contains_duplicate(nums):
    # Handle None input explicitly
    if nums is None:  # if the input itself is None, treat as empty
        return False  # no elements -> no duplicates
    
    # Fast paths for very small inputs
    n = len(nums)  # length may raise if nums isn't sized; we assume list-like in interviews
    if n < 2:  # 0 or 1 element cannot have duplicates
        return False
    
    # Optional: validate elements are hashable (ints are hashable; this protects weird inputs)
    # We avoid heavy validation per element for performance, but we can guard on common pitfalls.
    
    seen = set()  # track seen elements
    
    for x in nums:
        # If an interviewer pushes on "robustness", we can ensure hashability:
        try:
            # membership check; fails if x is unhashable
            if x in seen:  # average O(1) lookup
                return True
            seen.add(x)  # average O(1) insert
        except TypeError:
            # If elements are unhashable (e.g., a list), fall back to sorting by string or tuple cast.
            # Here we choose to convert lists/tuples to tuples; other types raise.
            if isinstance(x, list):
                t = tuple(x)
                if t in seen:
                    return True
                seen.add(t)
            else:
                # For truly unhashable/unsupported mixed types, conservatively continue or raise.
                # In interviews, you'd clarify expected input. We'll continue without crashing.
                continue
    
    return False  # no duplicates found

# --- Demonstration tests (not over-engineered) ---
if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))        # True
    print(contains_duplicate([1, 2, 3, 4]))        # False
    print(contains_duplicate([-1, -2, -3, -1]))    # True
    print(contains_duplicate([]))                  # False
    print(contains_duplicate(None))                # False
    print(contains_duplicate([[1,2], [3], [1,2]])) # True (list items handled by tuple cast)
        