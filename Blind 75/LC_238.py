# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

# Type 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        # left product
        p = 1
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]
        

        # right product
        p = 1
        for i in range(len(nums)-1, 0-1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        
        return output


# Type 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s
        # (answer[i] will store the product of elements to the left of i first)
        n = len(nums)                                     # length of the input
        answer = [1] * n                                  # output array
        
        # Pass 1: fill answer[i] with product of all elements to the left of i
        left = 1                                          # running product of left side
        for i in range(n):                                # iterate from left to right
            answer[i] = left                              # set left product for position i
            left *= nums[i]                               # update running left product
        
        # Pass 2: multiply by product of all elements to the right of i
        right = 1                                         # running product of right side
        for i in range(n - 1, -1, -1):                    # iterate from right to left
            answer[i] *= right                            # multiply by current right product
            right *= nums[i]                              # update running right product
        
        return answer                                     # final result


# CoderPad/HackerRank Test
# Product of Array Except Self - CoderPad/HackerRank style
# - Every line has comments to clarify intent
# - Includes lightweight I/O and extra edge-case notes

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    # Handle minimal constraints explicitly (though LC guarantees len >= 2)
    n = len(nums)                                        # number of elements
    if n == 0:                                           # if empty, return empty
        return []                                        # edge guard
    if n == 1:                                           # with one element, "except self" is ill-defined
        return [1]                                       # often defined as 1; not used in LC

    # Core O(1) extra space algorithm (excluding the output)
    answer = [1] * n                                     # initialize result with 1s
    
    # First pass: prefix products (left side)
    left = 1                                             # running product of elements before i
    for i in range(n):                                   # forward traversal
        answer[i] = left                                 # store left product at i
        left *= nums[i]                                  # update left for next index
    
    # Second pass: suffix products (right side)
    right = 1                                            # running product of elements after i
    for i in range(n - 1, -1, -1):                       # backward traversal
        answer[i] *= right                               # multiply stored left by right
        right *= nums[i]                                 # update right for previous index
    
    return answer                                        # final output

# --- Simple local tests (would be replaced by platform-specific harness) ---
if __name__ == "__main__":
    # Typical case
    print(product_except_self([1, 2, 3, 4]))             # [24, 12, 8, 6]
    # Includes zero(s)
    print(product_except_self([-1, 1, 0, -3, 3]))        # [0, 0, 9, 0, 0]
    # All negatives
    print(product_except_self([-2, -3, -4]))             # [12, 8, 6]
    # Repeated numbers
    print(product_except_self([2, 2, 2, 2]))             # [8, 8, 8, 8]
    # Edge-ish short arrays
    print(product_except_self([5, 0]))                   # [0, 5]