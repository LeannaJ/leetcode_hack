# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

# Type 1
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, right = 0, 0
        counts = collections.Counter()

        for right in range(len(s)):
            counts[s[right]] += 1
            max_char_n = counts.most_common(1)[0][1]

            if (right - left + 1) - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        
        return right - left + 1


# Type 2: only uppercase English letters 라는 가정이 있으므로 idx 0~25까지 배열로 처리
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = [0] * 26

        # Helper function to map character to index
        def idx(c: str) -> int:
            return ord(c) - ord('A')                     # 문자를 인덱스로 변환

        left = 0                                         # (1) 왼쪽 포인터 초기값 설정
        max_count = 0                                    # (2) 최대 등장 횟수 초기값 설정
        max_len = 0                                      # (3) 최대 길이(구하려는 값) 초기값 설정

        for right, ch in enumerate(s):                   
            j = idx(ch)                                  # (4) 문자를 인덱스로 변환
            freq[j] += 1                                 # (5) 문자의 등장 횟수 증가
            max_count = max(max_count, freq[j])          # (6) 최대 등장 횟수 업데이트

            window_len = right - left + 1                # (7) 윈도우 길이 계산
            
            if window_len - max_count > k:               # (8) 바꾸기 시도해야 하는 횟수 (윈도우 길이 - 최대 등장 횟수)가 k 초과이면
                freq[idx(s[left])] -= 1                  # (9) 기준인 왼쪽 포인터 문자의 등장 횟수 감소하면서 k에 맞을 때까지 윈도우 축소
                left += 1
                window_len = right - left + 1            # (10) 윈도우 길이 재계산
            
            max_len = max(max_len, window_len)           # (11) 최대 길이 업데이트

        return max_len


# CoderPad/HackerRank Test
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window with frequency count
        freq = [0] * 26
        left = 0
        max_count = 0
        best = 0

        def idx(c: str) -> int:
            return ord(c) - ord('A')

        for right, ch in enumerate(s):
            j = idx(ch)
            freq[j] += 1
            max_count = max(max_count, freq[j])

            # shrink window if replacements needed > k
            while (right - left + 1) - max_count > k:
                freq[idx(s[left])] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


# ---- Sample Tests ----
sln = Solution()
print(sln.characterReplacement("ABAB", 2))      # Expected 4
print(sln.characterReplacement("AABABBA", 1))   # Expected 4
print(sln.characterReplacement("AAAA", 2))      # Expected 4
print(sln.characterReplacement("ABCDE", 1))     # Expected 2
        
        