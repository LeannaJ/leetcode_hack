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