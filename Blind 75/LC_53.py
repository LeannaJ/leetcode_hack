# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both current sum and best sum to the first element
        curr = nums[0]  # current best sum ending at this index
        best = nums[0]  # global best sum so far
        
        # Iterate from second element to the end
        for x in nums[1:]:
            # Either start new subarray at x, or extend previous subarray with x
            curr = max(x, curr + x)  # local decision at each step
            # Update the global maximum
            best = max(best, curr)
        
        # Return the best sum after processing all elements
        return best


# CoderPad/HackerRank Test
# Time: O(n), Space: O(1)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = best = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)  # either start new or extend
            best = max(best, curr)
        return best

# Quick check
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(Solution().maxSubArray([1]))                      # 1
print(Solution().maxSubArray([5,4,-1,7,8]))             # 23