# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:            # s2가 s1의 순열을 포함하고 있는지 여부 확인
        
        # Edge case 1: if s1 is longer than s2, return False
        if len(s1) > len(s2):
            return False
        
        # Frequency Array
        need = [0] * 26                                         # (1) need 배열 초기화 (s1의 각 문자의 등장 횟수) --- 각 문자가 몇 번 나와야 하는지 저장 (타겟 빈도수)
        window = [0] * 26                                       # (2) window 배열 초기화 (s2의 각 문자의 등장 횟수) --- 각 문자가 몇 번 나왔는지 저장 (현재 빈도수)

        # Helper function to map character to index
        def idx(ch: str) -> int:                                # (3) 알파벳을 순서대로 번호로 변환 (알파벳을 0~25로 치환)
            return ord(ch) - ord('a')

        for ch in s1:                                           # (4) s1의 각 문자의 등장 횟수를 need 배열에 저장
            need[idx(ch)] += 1
        for ch in s2[:len(s1)]:                                 # (5) s2의 첫 len(s1)개 문자의 등장 횟수를 window 배열에 저장
            window[idx(ch)] += 1

        matches = 0                                             # (6) matches 변수 초기화 (s1과 s2의 각 문자의 등장 횟수가 같은지 확인)
        for i in range(26):                                     # (7) need와 window 배열이 같을 때는 무조건 matches 변수 업데이트
            if need[i] == window[i]:
                matches += 1
        
        if matches == 26:                                       # (8) matches가 26이면 알파벳 전체라서 당연히 True 반환
            return True
        
        left = 0                                                # (9) 나머지 당연하지 않은 경우들에서 조건 충족되는 거 찾기, 왼쪽 포인터(슬라이딩 윈도우 기준 왼쪽) 초기화
        for right in range(len(s1), len(s2)):                   # (10-1) 오른쪽 포인터(슬라이딩 윈도우 기준 오른쪽) 이동하여 window 확장
            in_idx = idx(s2[right])                             #        오른쪽 포인터 문자의 순서 번호 (치환값)
            out_idx = idx(s2[left])                             #        왼쪽 포인터 문자의 순서 번호 (치환값)
            left += 1                                           #        왼쪽 포인터를 하나씩 증가시키고,

            window[in_idx] += 1                                 # (10-2) 오른쪽 포인터 문자의 등장 횟수 증가 (현재 빈도수 업데이트)
            if window[in_idx] == need[in_idx]:                  #        현재 빈도수가 타겟 빈도수와 같으면 matches 증가
                matches += 1
            elif window[in_idx] - 1 == need[in_idx]:            #        현재 빈도수 - 1이 타겟 빈도수와 같으면 matches 감소
                matches -= 1
            
            window[out_idx] -= 1                                # (10-3) 왼쪽 포인터 문자의 등장 횟수 감소 (현재 빈도수 업데이트)
            if window[out_idx] == need[out_idx]:                #        현재 빈도수가 타겟 빈도수와 같으면 matches 증가
                matches += 1 
            elif window[out_idx] + 1 == need[out_idx]:          #        현재 빈도수 + 1이 타겟 빈도수와 같으면 matches 감소
                matches -= 1
            
            if matches == 26:                                   # (10-4) matches가 26이 될 때까지 반복 후, 알파벳 전체라서 당연히 True 반환
                return True
        
        return False


# CoderPad/HackerRank Test
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # frequency arrays for 26 lowercase letters
        need = [0] * 26
        window = [0] * 26
        def idx(c): return ord(c) - ord('a')
        
        for c in s1:
            need[idx(c)] += 1
        for c in s2[:len(s1)]:
            window[idx(c)] += 1
        
        matches = sum(need[i] == window[i] for i in range(26))
        if matches == 26:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            in_idx = idx(s2[right])
            out_idx = idx(s2[left])
            left += 1
            
            # add incoming char
            window[in_idx] += 1
            if window[in_idx] == need[in_idx]:
                matches += 1
            elif window[in_idx] - 1 == need[in_idx]:
                matches -= 1
            
            # remove outgoing char
            window[out_idx] -= 1
            if window[out_idx] == need[out_idx]:
                matches += 1
            elif window[out_idx] + 1 == need[out_idx]:
                matches -= 1
            
            if matches == 26:
                return True
        return False

# sample test
print(Solution().checkInclusion("ab", "eidbaooo"))  # True
print(Solution().checkInclusion("ab", "eidboaoo"))  # False