# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:                         # (1) 팰린드롬 확장 함수
            while left >= 0 and right < len(s) and s[left]== s[right]:    # (2) left, right 인덱스가 기본 조건을 만족하고, 문자열의 양쪽 끝이 같은 경우
                left -= 1                                                 # (3) left 인덱스를 왼쪽으로 확장
                right += 1                                                # (4) right 인덱스를 오른쪽으로 확장
            return s[left+1: right]                                       # (5) 검증된 팰린드롬 문자열까지만 반환(확장한 left, right 인덱스 사잇값만 반환)

        # Edge case 1: 문자열의 길이가 2 미만이거나 문자열이 팰린드롬인 경우
        if len(s) < 2 or s == s[::-1]:                                   
            return s                                                      # (6) 문자열의 길이가 2 미만이거나 문자열이 팰린드롬인 경우 문자열 반환

        result = ''
        for i in range(len(s) - 1):                                       # (7) 문자열의 각 인덱스를 순회
            result = max(result, expand(i, i+1), expand(i, i+2), key=len) # (8) 팰린드롬 확장 함수를 2칸, 3칸 짜리 기본 팰린드롬에 적용해 가장 긴 result 업데이트
        
        return result                                                     # (9) 가장 긴 팰린드롬 문자열 반환


# CoderPad/HackerRank Test