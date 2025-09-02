# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}                                         # (1) 문자의 마지막 등장 위치를 저장하는 딕셔너리
        left = 0                                              # (2) 현재 첫 번째 문자의 인덱스
        best = 0                                              # (3) 가장 긴 부분 문자열의 길이

        for right, ch in enumerate(s):                        # (4) 문자열의 각 문자를 순회
            if ch in last_pos and last_pos[ch] >= left:       # (5) 문자가 이미 등장했고, 이전에 등장한 위치가 left보다 크거나 같으면
                left = last_pos[ch] + 1                       # (6) left를 이전 등장 위치 + 1로 업데이트

            last_pos[ch] = right                              # (7) 문자의 마지막 등장 위치를 업데이트
            curr_len = right - left + 1                       # (8) 현재 부분 문자열의 길이
            if curr_len > best:                               # (9) 현재 부분 문자열의 길이가 가장 긴 부분 문자열의 길이보다 크면
                best = curr_len                               # (10) 가장 긴 부분 문자열의 길이를 업데이트
        
        return best                                           # (11) 가장 긴 부분 문자열의 길이를 반환
    

# Test
def length_of_longest_substring(s: str) -> int:
    
    # Edge case 1: s 가 None 일 경우
    if s is None:
        return 0
    
    last_pos = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_pos and last_pos[ch] >= left:
            left = last_pos[ch] + 1
        
        last_pos[ch] = right
        curr_len = right - left + 1
        if curr_len > best:
            best = curr_len
    
    return best

if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1)
        ("a", 1),
        ("aa", 1),
        ("ab", 2),
        ("abc", 3),
        ("abcd", 4),
    ]
    for s, expected in tests:
        got = length_of_longest_substring(s)
        print(f"s={s!r}, expected={expected}, got={got}")