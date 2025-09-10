# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # current_max: max product ending at current index
        # current_min: min product ending at current index (useful when next number is negative)
        # answer: global maximum product seen so far
        
        # Initialize with first element
        current_max = nums[0]   # current best positive product ending here
        current_min = nums[0]   # current worst (most negative) product ending here
        answer = nums[0]        # global best
        
        # Iterate from second element onward
        for x in nums[1:]:
            # If x is negative, swapping helps because min * negative -> big positive
            if x < 0:
                current_max, current_min = current_min, current_max  # swap
            
            # Extend or restart at x
            current_max = max(x, current_max * x)  # either start new at x or extend previous max
            current_min = min(x, current_min * x)  # either start new at x or extend previous min
            
            # Update global answer
            answer = max(answer, current_max)      # track the best seen so far
        
        return answer


# CoderPad/HackerRank Test
from typing import List

def max_product_subarray(nums: List[int]) -> int:
    """
    Return the maximum product of a contiguous subarray.
    Assumes nums is a non-empty list of integers.
    """
    # Initialize DP states
    current_max = nums[0]   # best product ending here
    current_min = nums[0]   # worst product ending here
    answer = nums[0]        # global best
    
    # Process each number in nums (starting from index 1)
    for x in nums[1:]:
        # If negative, swap max and min because sign flips
        if x < 0:
            current_max, current_min = current_min, current_max
        
        # Update states
        current_max = max(x, current_max * x)
        current_min = min(x, current_min * x)
        
        # Update global best
        answer = max(answer, current_max)
    
    return answer

# Simple test cases
if __name__ == "__main__":
    print(max_product_subarray([2,3,-2,4]))  # expect 6
    print(max_product_subarray([-2,0,-1]))  # expect 0
    print(max_product_subarray([-2]))  # expect -2
    print(max_product_subarray([0,2,-3,4,-1,2,1,-5,4]))  # expect 120
        