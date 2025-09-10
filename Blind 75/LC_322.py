# 322. Coin Change
# https://leetcode.com/problems/coin-change/

# Time: O(n * amount), Space: O(amount)
# n = number of coin denominations
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Guard: if amount is 0, no coin is needed
        if amount == 0:
            return 0
        # Initialize DP array with a large sentinel (amount+1 works as "infinite")
        dp = [amount + 1] * (amount + 1)  # dp[x] = min coins to make x
        dp[0] = 0  # base case: 0 amount needs 0 coins

        # Iterate all target amounts from 1..amount
        for x in range(1, amount + 1):
            # Try using each coin to reach amount x
            for c in coins:
                if x - c >= 0:                # only valid if coin does not overshoot
                    dp[x] = min(dp[x], dp[x - c] + 1)  # choose the best among options

        # If dp[amount] is still "infinite", it's impossible
        return dp[amount] if dp[amount] != amount + 1 else -1


# CoderPad/HackerRank Test
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    # Validate inputs (lightweight defensive checks)
    # 1) Empty coins list -> cannot make amount unless amount == 0
    if not coins:
        return 0 if amount == 0 else -1
    # 2) Negative amount is not meaningful; return -1 by convention
    if amount < 0:
        return -1
    # 3) Remove non-positive coins (0 or negative) and duplicates to avoid infinite loops / no-ops
    coins = [c for c in set(coins) if isinstance(c, int) and c > 0]
    if not coins:
        return 0 if amount == 0 else -1
    # 4) If amount == 0 -> 0 coins
    if amount == 0:
        return 0

    # Initialize DP array; use amount+1 as sentinel "infinity"
    dp = [amount + 1] * (amount + 1)  # dp[x] = min number of coins to make x
    dp[0] = 0  # base case

    # Bottom-up fill
    for x in range(1, amount + 1):            # iterate target amount
        for c in coins:                        # try every coin
            if x - c >= 0:                     # valid subproblem
                # Transition: use coin c once + best for (x - c)
                dp[x] = min(dp[x], dp[x - c] + 1)

    # If still "infinite", impossible
    return dp[amount] if dp[amount] != amount + 1 else -1

# --- Minimal interactive harness for CoderPad/HackerRank (optional) ---
# Input format (example):
# 3
# 1 2 5
# 11
# Where:
#   3         -> number of coins (n)
#   1 2 5     -> coin values
#   11        -> amount
if __name__ == "__main__":
    try:
        n = int(input().strip())              # number of coins
        coins = list(map(int, input().strip().split()))
        amount = int(input().strip())
        # Trim list to first n if extra tokens are provided
        coins = coins[:n]
        print(coin_change(coins, amount))
    except Exception:
        # In interview pads, keep failure mode simple
        print(-1)