# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1                       # (1) 현재 탐색 범위의 왼쪽과 오른쪽 인덱스(왼쪽은 초기값:0번, 오른쪽은 마지막값:전체길이-1번)

        while left <= right:                                 # (2) 탐색 범위가 존재하는 동안 반복
            mid = (left+right) // 2                          # (3) 현재 탐색 범위의 중간 인덱스
            
            if nums[left] == target:                         # (4) 왼쪽 값이 타겟과 일치하면 왼쪽 인덱스 반환
                return left
            if nums[right] == target:                        # (5) 오른쪽 값이 타겟과 일치하면 오른쪽 인덱스 반환
                return right
            if nums[mid] == target:                          # (6) 중간 인덱스의 값이 타겟과 일치하면 중간 인덱스 반환
                return mid
            
            if nums[left] <= nums[mid]:                      # (7) 왼쪽 값이 중간 값보다 작거나 같은 경우 (회전된 부분이 오른쪽에 있는 경우)
                if nums[left] <= target < nums[mid]:         # (8) 타겟이 왼쪽 값 포함, 왼쪽 값과 중간 값 사이에 있으면
                    right = mid - 1                          # (9) 오른쪽 포인터를 중간 포인터 - 1로 업데이트
                else:                                        
                    left = mid + 1                           # (10) 왼쪽 포인터를 중간 포인터 + 1로 업데이트
            else:                                            # (11) 왼쪽 값이 중간 값보다 큰 경우 (회전된 부분이 왼쪽에 있는 경우)
                if nums[mid] < target <= nums[right]:        # (12) 타겟이 오른쪽 값 포함, 중간 값과 오른쪽 값 사이에 있으면
                    left = mid + 1                           # (13) 왼쪽 포인터를 중간 포인터 + 1로 업데이트
                else:
                    right = mid - 1                          # (14) 오른쪽 포인터를 중간 포인터 - 1로 업데이트
        
        return -1                                            # (15) 타겟을 찾지 못했으면 -1 반환


# CoderPad/HackerRank Test
# Time: Average O(log n), Worst O(n) when many duplicates collapse order info
# Space: O(1)

from typing import List

def search_rotated_robust(nums: List[int], target: int) -> int:
    # Fast path for empty
    if not nums:  # handle empty list
        return -1  # not found
    
    left: int = 0  # left index
    right: int = len(nums) - 1  # right index
    
    while left <= right:  # standard binary search outer loop
        mid: int = (left + right) // 2  # middle index
        
        # Direct match check
        if nums[mid] == target:  # found target
            return mid  # return index
        
        # --- Duplicate edge handling ---
        # If endpoints equal mid, we cannot decide which side is sorted.
        # Shrink both ends to break ties (may degrade to O(n) in worst-case).
        if nums[left] == nums[mid] == nums[right]:  # ambiguous ordering due to duplicates
            left += 1  # shrink from left
            right -= 1  # shrink from right
            continue  # re-evaluate
        
        # --- Normal rotated binary search logic ---
        if nums[left] <= nums[mid]:  # left half is sorted (non-strict to include equal)
            if nums[left] <= target < nums[mid]:  # target is in the sorted left half
                right = mid - 1  # move right pointer left
            else:
                left = mid + 1  # move left pointer right
        else:  # right half is sorted
            if nums[mid] < target <= nums[right]:  # target is in the sorted right half
                left = mid + 1  # narrow to right half
            else:
                right = mid - 1  # narrow to left half
    
    # Not found
    return -1


# --- Extra tests for robustness (run in CoderPad) ---
if __name__ == "__main__":
    # Empty and single-element
    print(search_rotated_robust([], 5))                    # expected -1
    print(search_rotated_robust([10], 10))                # expected 0
    
    # Standard rotated cases
    print(search_rotated_robust([4,5,6,7,0,1,2], 0))      # expected 4
    print(search_rotated_robust([6,7,1,2,3,4,5], 3))      # expected 4
    
    # Negative, large values
    print(search_rotated_robust([1000000, 2000000, -5, 0, 1, 2], -5))  # expected 2
    
    # With duplicates (not required by LC33 but robust)
    print(search_rotated_robust([2,2,2,3,4,2], 3))        # expected 3
    print(search_rotated_robust([1,1,1,1,1], 2))          # expected -1