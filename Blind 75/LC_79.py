# 79. Word Search
# https://leetcode.com/problems/word-search/

# Time: O(m * n * 4^L) worst-case
# Space: O(L) recursion, O(1) extra due to in-place marking

from collections import Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get board dimensions
        m, n = len(board), len(board[0])

        # Quick frequency pruning: if board lacks any needed char, return False
        board_counter = Counter(ch for row in board for ch in row)
        word_counter = Counter(word)
        for ch, cnt in word_counter.items():
            if board_counter[ch] < cnt:
                return False  # Not enough occurrences of 'ch' on the board

        # Optional heuristic: search the word in a direction that starts with a rarer letter
        # If last char is rarer than first char on the board, reverse the word
        if board_counter[word[-1]] < board_counter[word[0]]:
            word = word[::-1]

        # Directions: up, down, left, right
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # DFS function: try to match word[k] at position (i, j)
        def dfs(i: int, j: int, k: int) -> bool:
            # If we've matched all characters, success
            if k == len(word):
                return True

            # Boundary checks
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            # If current cell doesn't match the needed char, fail
            if board[i][j] != word[k]:
                return False

            # Mark this cell as visited by temporarily altering the board
            temp = board[i][j]     # save original char
            board[i][j] = '#'      # mark as visited (sentinel)

            # Explore all 4 directions
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj
                if dfs(ni, nj, k + 1):
                    board[i][j] = temp  # restore before returning
                    return True

            # Backtrack: restore the character
            board[i][j] = temp
            return False

        # Try starting from every cell that matches word[0]
        first = word[0]
        for i in range(m):
            for j in range(n):
                if board[i][j] == first and dfs(i, j, 0):
                    return True

        return False


# CoderPad/HackerRank Test
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#"  # mark visited

            for di, dj in directions:
                if dfs(i+di, j+dj, k+1):
                    board[i][j] = temp
                    return True

            board[i][j] = temp  # backtrack
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# --- Simple test run ---
if __name__ == "__main__":
    sol = Solution()

    board1 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    print(sol.exist(board1, "ABCCED"))  # True
    print(sol.exist(board1, "SEE"))     # True
    print(sol.exist(board1, "ABCB"))    # False