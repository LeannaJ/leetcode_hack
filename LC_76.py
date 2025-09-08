# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)                                                 # (1) t의 각 문자의 등장 횟수를 보여주는 Counter 객체(dict 형태)
        required = len(t_count)                                              # (2) t_count의 길이를 계산
        left, right = 0, 0                                                   # (3) 왼쪽과 오른쪽 포인터를 초기화
        formed = 0                                                           # (4) t_count와 매칭되는 문자 개수를 초기화
        window_count = {}                                                    # (5) 윈도우 내 각 문자의 등장 횟수를 dict 형태로 저장
        min_length = (float('inf'), None, None)                              # (6) 최소값을 찾을 때, 시작을 무한대로 잡으면 어떤 값이 와도 더 작기 때문에 항상 갱신 가능 (tuple: (최소값, 시작인덱스, 끝인덱스))

        while right < len(s):                                                # (7) 오른쪽 포인터 이동하여 window 확장: 오른쪽 포인터가 s의 길이 끝까지 갈 동안 반복 (조건 충족하는 경우 찾기)
            char = s[right]                                                  
            window_count[char] = window_count.get(char, 0) + 1               # (7-1) window_count dict 내 key, char가 등장하는 횟수를 계산 (해당 key가 0으로 시작, 1을 더한다)

            if char in t_count and window_count[char] == t_count[char]:      # (7-2) window_count 문자와 t_count 매칭 문자가 같으면 -> formed 매칭 문자 개수에 1 추가
                formed += 1
            
            while left <= right and formed == required:                      # (8) 왼쪽 포인터 이동하여 window 축소: 조건 충족이 깨지기 전까지 왼쪽 포인터를 오른쪽으로 이동 (최소 길이 찾기)
                char = s[left]

                if right - left + 1 < min_length[0]:                         # (8-1) 조건 충족이 된 경우, 길이 계산해보고 최소 길이 업데이트
                    min_length = (right - left + 1, left, right)

                window_count[char] -= 1                                      # (8-2) window_count 문자 등장 횟수 1 감소시켜봤을 때
                if char in t_count and window_count[char] < t_count[char]:   #       window_count 문자 등장 횟수가 t_count 문자 등장 횟수보다 작으면 -> formed 매칭 문자 개수에 1 감소
                    formed -= 1
                
                left += 1                                                    # (8-3) 왼쪽 포인터 추가 이동하여 다시 조건 충족하는지 확인
            right += 1                                                       # (7-3) 조건 충족이 안 된 경우, 오른쪽 포인터 추가 이동하여 다시 window 확장

        return "" if min_length[0] == float('inf') else s[min_length[1]: min_length[2] + 1]     # (9) 최소 길이가 무한대이면 빈 문자열 반환, 아니면 최소 길이 문자열 반환


# CoderPad/HackerRank Test
from collections import Counter

def min_window_substring(s: str, t: str) -> str:
    
    # Edge case 1: if t is falsy value, return ""
    if not t:
        return ""

    # Edge case 2: if t is longer than s, impossible
    if len(t) > len(s):
        return ""
    
    t_count = Counter(t)
    required = len(t_count)
    
    left, right = 0, 0
    formed = 0
    window_count = {}
    min_length = (float("inf"), None, None)
    
    while right < len(s):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        while left <= right and formed == required:
            char = s[left]
            
            if right - left + 1 < min_length[0]:
                min_length = (right - left + 1, left, right)
            
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    if min_length[0] == float("inf"):
        return ""
    else:
        return s[min_length[1]: min_length[2] + 1]

print(min_window_substring("ADOBECODEBANC", "ABC"))  # Expected "BANC"
print(min_window_substring("a", "a"))                # Expected "a"
print(min_window_substring("a", "aa"))               # Expected ""
print(min_window_substring("", "ABC"))               # Expected ""
print(min_window_substring("ABC", ""))               # Expected ""


# If constraints are changed?
"""
Edge case considerations for character set variations:

1. If digits or special characters are included:
   - Example: s = "a#b1c2A", t = "1c"
   - Works without modification since dict/Counter can store any character as keys.

2. If Unicode characters (e.g., Korean, emoji) are included:
   - Example: s = "가나다abc😊", t = "나😊"
   - Still works without changes, because dict/Counter supports Unicode.
   - Time complexity remains O(|s| + |t|), even if the character set is larger.
   - The algorithm does not change, only the possible key space increases.

3. If the problem is case-insensitive:
   - Example: s = "aAbBcC", t = "abc"
   - Preprocess both strings by converting to lowercase (or uppercase).
   - For example:
       s = s.lower()
       t = t.lower()
"""