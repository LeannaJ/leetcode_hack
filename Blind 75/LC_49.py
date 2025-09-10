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
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


# Quick test
if __name__ == "__main__":
    example = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(example))
    # Expected: [["eat","tea","ate"], ["tan","nat"], ["bat"]]