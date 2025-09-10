# 15. 3Sum
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):

            # Edge case 1: 중복된 값 제거
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return results


# CoderPad/HackerRank Test
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    # Sort to enable two-pointer scanning and deduplication
    nums.sort()
    n = len(nums)
    res: List[List[int]] = []

    # Iterate each index as the anchor of the triplet
    for i in range(n - 2):
        # Skip duplicate anchors to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        # Two-pointer sweep
        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s < 0:
                # Need a larger sum -> move left
                left += 1
            elif s > 0:
                # Need a smaller sum -> move right
                right -= 1
            else:
                # Found a valid triplet
                res.append([nums[i], nums[left], nums[right]])

                # Move left forward skipping duplicates
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Move right backward skipping duplicates
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res


# --- Minimal CoderPad I/O harness ---
def main():
    # Read a single line of space-separated integers
    line = input().strip()
    if not line:
        print([])  # empty input => empty result
        return
    nums = list(map(int, line.split()))
    print(three_sum(nums))

# Uncomment to run in CoderPad:
# if __name__ == "__main__":
#     main()