# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search on rotated sorted array without duplicates
        # Invariant: the minimum is always within [left, right]
        left: int = 0  # left boundary of the search window
        right: int = len(nums) - 1  # right boundary of the search window

        # If the array is already sorted (not rotated), the first element is the minimum
        if nums[left] <= nums[right]:
            return nums[left]  # early exit for unrotated array

        # Perform binary search to locate the rotation pivot (minimum element)
        while left < right:
            mid: int = (left + right) // 2  # middle index

            # If mid element is greater than the rightmost element,
            # the minimum lies in the right half (excluding mid)
            if nums[mid] > nums[right]:
                left = mid + 1  # move left boundary to the right of mid
            else:
                # Otherwise, the minimum lies in the left half (including mid)
                right = mid  # keep mid since it could be the minimum

        # When left == right, we've found the minimum
        return nums[left]


# CoderPad/HackerRank Test
from typing import List, Optional

def find_min_rotated(nums: List[int]) -> Optional[int]:
    """
    Return the minimum in a rotated sorted array without duplicates.
    Defensive: handle empty input gracefully by returning None.
    """
    # Validate input list
    if nums is None:  # handle None defensively
        # In interviews, you can also raise ValueError("nums is None")
        return None  # returning None for robustness
    if len(nums) == 0:  # empty list edge case
        return None  # no minimum exists

    # Single element edge case: the only element is the minimum
    if len(nums) == 1:
        return nums[0]  # directly return the single value

    left: int = 0  # left boundary pointer
    right: int = len(nums) - 1  # right boundary pointer

    # Already sorted (not rotated) optimization
    if nums[left] <= nums[right]:
        return nums[left]  # first element is the minimum

    # Standard binary search loop to find the rotation pivot
    while left < right:
        mid: int = (left + right) // 2  # compute mid index

        # Key comparison: nums[mid] vs nums[right]
        if nums[mid] > nums[right]:
            # Minimum is strictly to the right of mid
            left = mid + 1  # discard left..mid
        else:
            # Minimum is within left..mid
            right = mid  # keep mid since it might be the answer

    # Converged to the minimum index
    return nums[left]


# --- Below are simple harness examples you'd type in CoderPad/HackerRank to test quickly ---

if __name__ == "__main__":
    # Basic tests including edge cases
    samples = [
        [3, 4, 5, 1, 2],        # rotated, min=1
        [4, 5, 6, 7, 0, 1, 2],  # rotated, min=0
        [11, 13, 15, 17],       # not rotated, min=11
        [2],                    # single element, min=2
        [],                     # empty -> None
        [1, 2, 3, 4, 5],        # sorted, min=1
    ]

    # Print results to verify correctness
    for arr in samples:
        # Show input and output for quick manual validation
        print(f"input={arr} -> min={find_min_rotated(arr)}")
        