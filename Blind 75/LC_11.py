# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left: int = 0                                                   # (1) 왼쪽 포인터 초기값 0부터 시작
        right: int = len(height) - 1                                    # (2) 오른쪽 포인터 초기값 리스트 길이 - 1부터 시작

        max_area = 0                                                    # (3) 최대 넓이 초기값 0
        
        while left < right:
            area = (right - left) * min(height[right], height[left])    # (4) 넓이 계산

            if area > max_area:                                         # (5) 넓이가 최대 넓이보다 크면 최대 넓이 업데이트
                max_area = area
            
            if height[left] < height[right]:                            # (6) 왼쪽 포인터가 오른쪽 포인터보다 작으면 왼쪽 포인터가 높이값
                left += 1                                               # (7) 왼쪽 포인터 1 증가시켜서 다음 인덱스로 이동
            else:                                                       # (8) 왼쪽 포인터가 오른쪽 포인터보다 크거나 같으면 오른쪽 포인터가 높이값
                right -= 1                                              # (9) 오른쪽 포인터 1 감소시켜서 다음 인덱스로 이동
        
        return max_area                                                 # (10) 최대 넓이 반환


# CoderPad/HackerRank Test

# Read: space-separated ints on one line
# Print: maximum water area

from typing import List

def max_area(height: List[int]) -> int:
    # Two-pointer linear scan: O(n) time, O(1) space
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        # Width between the two lines
        width = right - left
        # Height limited by the shorter line
        h = min(height[left], height[right])
        # Update best area
        area = h * width
        if area > best:
            best = area
        # Move the pointer at the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best

def main():
    # Simple input: "1 8 6 2 5 4 8 3 7"
    line = input().strip()
    if not line:
        print(0); return
    arr = [int(x) for x in line.replace(',', ' ').replace('[',' ').replace(']',' ').split()]
    if len(arr) < 2:
        print(0); return
    print(max_area(arr))

if __name__ == "__main__":
    main()


# CoderPad Enhanced (with edge-case handling)
from typing import List

def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = h * width
        if area > best:
            best = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

def parse_line(s: str) -> List[int]:
    # Accepts: "1 8 6 2 5 4 8 3 7" or "[1,8,6,2,5,4,8,3,7]"
    s = s.strip().replace('[',' ').replace(']',' ').replace(',',' ')
    out = []
    for tok in s.split():
        try:
            out.append(int(tok))
        except ValueError:
            # Ignore any non-integer token gracefully
            pass
    return out

def main():
    try:
        line = input().strip()
    except EOFError:
        print(0); return
    nums = parse_line(line)
    if len(nums) < 2:
        print(0); return
    print(max_area(nums))

if __name__ == "__main__":
    main()