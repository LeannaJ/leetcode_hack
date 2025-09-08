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