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

from typing import Optional, Tuple, List

def longest_palindrome(s: Optional[str]) -> str:
    # Guard: handle None input explicitly
    if s is None:
        # In many interview platforms, returning empty string is acceptable for None
        return ""
    # Guard: empty or single-character strings are already palindromic
    if len(s) <= 1:
        return s

    # Local helper: expand around center and return inclusive bounds (l, r)
    def expand_from_center(left: int, right: int) -> Tuple[int, int]:
        # Expand while within bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1           # move left pointer outward
            right += 1          # move right pointer outward
        # After overshooting one step, move back to the last valid palindrome window
        return left + 1, right - 1

    best_l, best_r = 0, 0  # best window [best_l, best_r]

    # Iterate every possible center: index i for odd, gap (i, i+1) for even
    for i in range(len(s)):
        l1, r1 = expand_from_center(i, i)       # odd-length
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1

        l2, r2 = expand_from_center(i, i + 1)   # even-length
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2

    # Slice is safe even if best_l == best_r
    return s[best_l:best_r + 1]


# Minimal test harness
def _run_tests():
    # Each test: (input, expected_set) - allow multiple correct answers if ambiguous
    tests: List[tuple[str, set]] = [
        ("babad", {"bab", "aba"}),     # multiple valid answers
        ("cbbd", {"bb"}),
        ("a", {"a"}),
        ("ac", {"a", "c"}),
        ("", {""}),                    # empty string edge case
        ("aaaa", {"aaaa"}),            # uniform characters
        ("abaxabaxabb", {"baxabaxab"}),# classic center-expansion check
        ("abcdeffedxyz", {"deffed"}),  # even-length center
    ]

    # None input check (platform dependent; here we expect empty string)
    none_result = longest_palindrome(None)
    print("Input: None ->", repr(none_result), "OK" if none_result == "" else "FAIL")

    for s, expected in tests:
        result = longest_palindrome(s)
        ok = result in expected
        print(f"Input: {s!r:15}  Output: {result!r:10}  {'OK' if ok else 'FAIL'}")

if __name__ == "__main__":
    # In CoderPad/HackerRank, you can comment this out if the runner provides its own entrypoint.
    _run_tests()