# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)                            # (1) 애너그램 맵을 생성 (defaultdict를 사용하여 초기값을 빈 리스트로 설정)

        for s in strs:
            key = ''.join(sorted(s))                               # (2) 문자열을 정렬하여 키로 사용
            anagram_map[key].append(s)                             # (3) 키에 해당하는 리스트에 문자열 추가
        
        return list(anagram_map.values())                          # (4) 애너그램 맵의 값을 리스트로 반환
    

# CoderPad/HackerRank Test
def group_anagrams(strs):

    # Edge case 1: strs 가 falsy value일 경우
    if not strs:
        return []
    
    anagram_map = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))
        anagram_map[key].append(s)
    
    return list(anagram_map.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([]))
print(group_anagrams(["a"]))
print(group_anagrams([""]))