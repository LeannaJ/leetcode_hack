# 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/

# Idea: Use length-prefix encoding: "<len>#<string>"
# This works for any character (including '#') because '#' only separates the length and the payload.

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        # We will build the encoded string using length + '#' + s for each s
        # Example: ["leet","code"] -> "4#leet4#code"
        res = []  # list for efficient concatenation
        for s in strs:
            # Convert length to string, add delimiter '#', then the string itself
            res.append(f"{len(s)}#{s}")
        # Join all parts into one single string
        return "".join(res)
        
    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        i = 0                 # read pointer
        out = []              # result list
        n = len(s)            # total length of the encoded string
        while i < n:
            # 1) Read the length prefix up to the delimiter '#'
            j = i             # position to scan for '#'
            # Move j forward until we find the '#'
            while s[j] != '#':
                j += 1
            # Parse the substring [i, j) as an integer length
            length = int(s[i:j])
            # 2) The string content starts at j+1 and spans 'length' characters
            start = j + 1
            end = start + length
            # Extract the original string
            out.append(s[start:end])
            # 3) Move i to the next block
            i = end
        return out


# CoderPad/HackerRank Test
from typing import List, Optional

class SafeCodec:
    def encode(self, strs: Optional[List[str]]) -> str:
        """
        Encode list of strings into a single string.
        
        - Accepts None -> treats as empty list.
        - Accepts any Unicode content safely (length is in code points).
        """
        # If input is None, treat as empty list for robustness
        if strs is None:
            strs = []
        # Validate that all items are strings
        # (If not, coerce to str for pragmatism in live settings)
        parts: List[str] = []   # gather chunks for efficient join
        for s in strs:
            # Coerce non-str to str to avoid runtime error in mixed inputs
            if not isinstance(s, str):
                s = str(s)
            # Append "<length>#<payload>"
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: Optional[str]) -> List[str]:
        """
        Decode a single string back to list of strings.
        
        - Accepts None -> returns [].
        - Performs minimal format validation:
          * length prefix must be digits
          * '#' must exist
          * payload must have enough characters
        - Raises ValueError with a helpful message on malformed input.
        """
        if s is None or s == "":
            # None or empty encoded string represents empty list
            return []
        
        out: List[str] = []   # result accumulator
        i: int = 0            # read cursor
        n: int = len(s)       # total length
        
        while i < n:
            # Find the delimiter '#'
            j = i
            # Ensure there is at least one digit for the length
            if j >= n or not s[j].isdigit():
                raise ValueError(f"Malformed input at position {i}: expected length digits.")
            # Scan digits until we hit '#'
            while j < n and s[j].isdigit():
                j += 1
            # After digits, we must have a '#'
            if j >= n or s[j] != '#':
                raise ValueError(f"Malformed input at position {j}: missing '#' after length.")
            # Parse length
            try:
                length = int(s[i:j])
            except Exception as e:
                raise ValueError(f"Invalid length at [{i}:{j}]: {s[i:j]}") from e
            # Compute payload bounds
            start = j + 1
            end = start + length
            # Validate payload bounds
            if end > n:
                raise ValueError(
                    f"Truncated payload: need {length} chars from {start}, but string ends at {n}."
                )
            # Slice the payload
            out.append(s[start:end])
            # Advance cursor
            i = end
        
        return out

# ---------------------------
# Minimal inline tests (can be run in CoderPad/HackerRank)
# ---------------------------
if __name__ == "__main__":
    codec = SafeCodec()
    
    # Basic cases
    original = ["leet", "code", "!", "", "#hash#", "멀티바이트😊", "123"]
    encoded = codec.encode(original)
    decoded = codec.decode(encoded)
    print("Encoded:", encoded)        # For quick visibility
    print("Decoded OK:", decoded == original)

    # Edge cases
    print(codec.decode(codec.encode([])))          # []
    print(codec.decode(codec.encode([""])))        # [""]
    print(codec.decode(codec.encode(["#"])))       # ["#"]
    print(codec.decode(codec.encode(["", "", ""])))# ["", "", ""]
    
    # Robustness: mixed types -> coerced to str
    mixed = ["a", 123, None, True]
    print(codec.decode(codec.encode(mixed)))       # ["a", "123", "None", "True"]
        