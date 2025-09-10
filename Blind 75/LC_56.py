# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])                          # (1) 인터벌을 시작 시간을 기준으로 정렬
        
        merged: List[List[int]] = []                                  # (2) 병합된 인터벌을 저장하는 리스트

        for start, end in intervals:
            if not merged or start > merged[-1][1]:                   # (3) 병합된 리스트가 비어있거나, 현재 인터벌의 시작 시간이 병합된 리스트의 마지막 인터벌의 종료 시간보다 크면
                merged.append([start, end])                           # (4) 병합된 리스트에 현재 인터벌을 추가
            else:                                                     # (5) 병합된 리스트의 마지막 인터벌의 종료 시간이 현재 인터벌의 시작 시간보다 크거나 같으면
                merged[-1][1] = max(merged[-1][1], end)               # (6) 병합된 리스트의 마지막 인터벌의 종료 시간을 현재 인터벌의 종료 시간과 비교하여 더 큰 값으로 업데이트
        
        return merged
    

# CoderPad/HackerRank Test
from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:

    # Edge case 1: intervals 가 falsy value인 경우
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])

    merged: List[List[int]] = []

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    return merged

if __name__ == "__main__":
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
    print(merge_intervals([[1,4],[4,5]]))
    print(merge_intervals([[1,5]]))
    print(merge_intervals([[1,5],[5,6]]))
    print(merge_intervals([[1,5],[5,6],[6,7]]))
