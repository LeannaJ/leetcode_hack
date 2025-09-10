# 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):                                          # (1) nums 리스트를 순회하며 각 요소와 인덱스를 가져옴
            complement = target - n                                           # (2) 현재 요소의 보수를 계산

            if complement in nums[i+1:]:                                      # (3) 보수가 리스트에 있는 경우
                return [nums.index(n), nums[i+1:].index(complement)+ (i+1)]   # (4) 현재 요소의 인덱스와 보수의 인덱스를 반환


# CoderPad/HackerRank Test
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, val in enumerate(nums):
        complement = target - val
        if complement in seen:
            return [seen[complement], i]
        seen[val] = i
    return []  # problem guarantees one solution, so normally unreachable

# Example runs
print(two_sum([2,7,11,15], 9))   # [0,1]
print(two_sum([3,2,4], 6))       # [1,2]
print(two_sum([3,3], 6))         # [0,1]