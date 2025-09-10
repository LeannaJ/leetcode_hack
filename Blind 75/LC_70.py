# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # Handle base cases directly:
        # If n is 0 (not typical per constraints but safe), there is 1 way (do nothing).
        if n <= 1:
            return 1
        
        # prev2 holds f(i-2), initialized to f(1) = 1
        prev2 = 1
        # prev1 holds f(i-1), initialized to f(2) = 2
        prev1 = 2
        
        # Iterate from step 3 up to n, computing current = prev1 + prev2
        for _ in range(3, n + 1):
            # current ways equals sum of the previous two states
            current = prev1 + prev2
            # Shift window: f(i-2) <- f(i-1)
            prev2 = prev1
            # Shift window: f(i-1) <- f(i)
            prev1 = current
        
        # When loop ends, prev1 holds f(n)
        return prev1

    
# CoderPad/HackerRank Test
def climb_stairs(n: int) -> int:
    # Base cases
    if n <= 1:
        return 1
    
    # prev2 = f(1), prev1 = f(2)
    prev2, prev1 = 1, 2
    
    # Iteratively build up to n
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

# Quick test inside CoderPad (you can comment this out after demo)
if __name__ == "__main__":
    print(climb_stairs(2))  # Expected 2
    print(climb_stairs(3))  # Expected 3
    print(climb_stairs(5))  # Expected 8