# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert list to set for O(1) membership checks
        word_set = set(wordList)  # words we can still use
        
        # If endWord is not present, no transformation is possible
        if endWord not in word_set:
            return 0
        
        # Standard BFS queue: (current_word, distance)
        q = deque()
        q.append((beginWord, 1))  # distance counts the beginWord itself
        
        # While there are nodes to process
        while q:
            current, dist = q.popleft()  # pop the leftmost element (FIFO)
            
            # If we reached the target, return the distance
            if current == endWord:
                return dist
            
            # Try changing each position to 'a'..'z'
            # This generates all neighbors differing by exactly one character
            for i in range(len(current)):
                # For each letter 'a'..'z' try to form a new word
                for c in map(chr, range(ord('a'), ord('z') + 1)):
                    # Skip if the character is the same; optional micro-optimization
                    if c == current[i]:
                        continue
                    
                    # Build the candidate word
                    candidate = current[:i] + c + current[i+1:]
                    
                    # If candidate is available, push to queue and remove from set
                    if candidate in word_set:
                        word_set.remove(candidate)  # mark visited
                        q.append((candidate, dist + 1))  # enqueue with incremented distance
        
        # No path found
        return 0


# CoderPad/HackerRank Test
from collections import deque
from typing import List

def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Return the length of the shortest transformation sequence from beginWord to endWord.
    A transformation changes exactly one letter and must produce a word inside wordList.
    The length counts both beginWord and endWord if reachable.
    """
    # --- Input validation & early exits ---
    # Guard against None inputs
    if beginWord is None or endWord is None or wordList is None:
        return 0  # invalid input
    
    # Convert to strings just in case; strip spaces
    beginWord = str(beginWord).strip()
    endWord = str(endWord).strip()
    
    # Empty strings are invalid
    if not beginWord or not endWord:
        return 0
    
    # All words must be same length; if not, impossible
    if len(beginWord) != len(endWord):
        return 0
    
    # Build a set for O(1) lookup
    word_set = set(wordList)
    
    # endWord must be present to be reachable
    if endWord not in word_set:
        return 0
    
    # If begin equals end, the shortest length is 1 (itself)
    if beginWord == endWord:
        return 1
    
    # --- BFS setup ---
    q = deque()
    q.append((beginWord, 1))  # start distance is 1 because we count beginWord
    # To avoid revisiting beginWord via wordList, ensure it's not in word_set
    if beginWord in word_set:
        word_set.remove(beginWord)
    
    # --- BFS traversal ---
    while q:
        word, dist = q.popleft()
        
        # Generate neighbors by changing each position to 'a'..'z'
        for i in range(len(word)):
            # Pre-slice for speed (micro-optimization)
            prefix = word[:i]
            suffix = word[i+1:]
            
            # Try all 26 letters
            for code in range(ord('a'), ord('z') + 1):
                ch = chr(code)
                # Skip same character to avoid redundant string building
                if ch == word[i]:
                    continue
                
                candidate = prefix + ch + suffix
                
                # If we've reached the end, return dist + 1
                if candidate == endWord:
                    return dist + 1
                
                # If candidate is valid and unvisited, enqueue and mark visited
                if candidate in word_set:
                    word_set.remove(candidate)  # mark visited
                    q.append((candidate, dist + 1))
    
    # No path found
    return 0


# --- Minimal inline tests (you can comment these out in an interview) ---
if __name__ == "__main__":
    # Classic example
    print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Expected: 5
    # No endWord in list
    print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]))        # Expected: 0
    # begin == end
    print(ladder_length("same", "same", ["same"]))                              # Expected: 1
    # Different lengths -> impossible
    print(ladder_length("hit", "hits", ["hits"]))                               # Expected: 0