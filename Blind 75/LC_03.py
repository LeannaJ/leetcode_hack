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
    

# CoderPad/HackerRank Test

def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    Sliding window + hashmap approach.
    Time: O(n), Space: O(min(n, charset))
    """
    if not s:  # handle empty string
        return 0

    last_idx = {}      # store last seen index of each character
    left = 0           # left boundary of sliding window
    max_len = 0        # track best length

    for right, ch in enumerate(s):
        if ch in last_idx and last_idx[ch] >= left:
            # move left pointer right after the previous duplicate
            left = last_idx[ch] + 1
        last_idx[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# Simple tests (for CoderPad)
if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # expect 3 ("abc")
    print(length_of_longest_substring("bbbbb"))     # expect 1 ("b")
    print(length_of_longest_substring("pwwkew"))    # expect 3 ("wke")
    print(length_of_longest_substring(""))          # expect 0
    print(length_of_longest_substring("au"))        # expect 2 ("au")
    print(length_of_longest_substring("abba"))      # expect 2 ("ab" or "ba")