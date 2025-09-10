# 704. Binary Search
# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums, target):
        # Initialize search boundaries
        left = 0                       # left pointer starts at the beginning
        right = len(nums) - 1          # right pointer starts at the end

        # Standard iterative binary search
        while left <= right:           # continue while there is a valid search window
            mid = (left + right) // 2  # pick middle index (integer division)

            if nums[mid] == target:    # found the target
                return mid

            if nums[mid] < target:     # target is in the right half
                left = mid + 1
            else:                      # target is in the left half
                right = mid - 1

        # target not found
        return -1


# CoderPad/HackerRank Test
# Time: O(log n)
# Space: O(1)

def binary_search(nums, target):
    """
    Perform iterative binary search on a sorted (ascending) list.

    Args:
        nums (List[int]): sorted in ascending order
        target (int): value to find
    Returns:
        int: index of target if found; otherwise -1
    """
    # ---- light-weight edge handling ----
    if not nums:                       # handle empty list (None or [])
        return -1
    # Optional: if inputs might be unsorted in a real system, we could guard,
    # but in LC704 it's guaranteed sorted. We'll keep it minimal and skip heavy checks.

    left = 0                           # left boundary (inclusive)
    right = len(nums) - 1              # right boundary (inclusive)

    while left <= right:               # valid search window
        mid = (left + right) // 2      # middle index

        # Compare and narrow the search window
        if nums[mid] == target:
            return mid                  # found
        if nums[mid] < target:
            left = mid + 1              # go right
        else:
            right = mid - 1             # go left

    return -1                           # not found

# ---- Minimal sanity tests (can be shown/run in CoderPad) ----
if __name__ == "__main__":
    # Typical cases
    print(binary_search([-1,0,3,5,9,12], 9))   # expected 4
    print(binary_search([-1,0,3,5,9,12], 2))   # expected -1

    # Edge cases
    print(binary_search([], 1))                # expected -1 (empty list)
    print(binary_search([5], 5))               # expected 0 (single element match)
    print(binary_search([5], -3))              # expected -1 (single element non-match)