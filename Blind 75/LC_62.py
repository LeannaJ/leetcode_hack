# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

# Type 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D DP array of size n filled with 1s
        # dp[j] represents the number of ways to reach column j in the current row
        dp = [1] * n
        
        # Iterate over rows starting from the second row (index 1)
        for _ in range(1, m):
            # Update each column starting from column 1
            for j in range(1, n):
                # Current cell = ways from top (dp[j]) + ways from left (dp[j-1])
                dp[j] += dp[j - 1]
        # The last element holds the number of paths to bottom-right
        return dp[-1]


# Type 2
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We compute C(m+n-2, k) where k = min(m-1, n-1) for fewer multiplicative steps
        total_steps = m + n - 2  # total moves: down + right
        k = min(m - 1, n - 1)    # choose the smaller to minimize loop iterations
        
        # Multiplicative computation of binomial coefficient to avoid large factorials
        # res = product_{i=1..k} (total_steps - k + i) / i
        res = 1
        for i in range(1, k + 1):
            # Multiply by numerator (an increasing sequence)
            res *= (total_steps - k + i)
            # Divide by i exactly (division is exact at each step)
            res //= i
        return res


# CoderPad/HackerRank Test
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP: number of ways to reach each cell
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]

# Example test cases (safe for CoderPad)
print(Solution().uniquePaths(3, 7))  # 28
print(Solution().uniquePaths(3, 2))  # 3
print(Solution().uniquePaths(7, 3))  # 28
print(Solution().uniquePaths(3, 3))  # 6