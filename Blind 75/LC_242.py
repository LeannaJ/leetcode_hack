# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Build frequency dictionary for s
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Decrease counts based on t
        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] -= 1
        
        # If all counts balanced, return True
        return True


# CoderPad/HackerRank Test
from typing import Optional

def is_anagram(s: Optional[str], t: Optional[str]) -> bool:
    # Validate inputs are strings
    if not isinstance(s, str) or not isinstance(t, str):
        return False
    
    # Quick length check
    if len(s) != len(t):
        return False
    
    # Early return if same reference
    if s is t:
        return True
    
    # Count frequencies in s
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # Decrease frequencies using t
    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
    
    # All counts must be zero at this point
    return True


# Minimal demo
if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
    print(is_anagram("", ""))                # True
    print(is_anagram(None, "abc"))           # False
        