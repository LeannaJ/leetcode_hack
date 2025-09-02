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
def search_rotated(nums, target):
    # Edge case 1: nums 가 None 일 경우
    if not nums:
        return -1
    # Edge case 2: nums 가 1개일 경우
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        #Quick Boundary Checks
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def main():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())

    # Validation Check
    if len(nums) < n:                                       # (1) nums 의 길이가 n 보다 작으면 pass
        pass
    nums = nums[:n]                                         # (2) nums 의 길이가 n 보다 크거나 같으면 nums 의 첫 n 개의 요소만 사용 (enforce exactly n numbers (trim or ignore extras))

    print(search_rotated(nums, target))

if __name__ == "__main__":
    main()        