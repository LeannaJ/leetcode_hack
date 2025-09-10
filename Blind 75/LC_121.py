# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min_price with positive infinity so any price will be smaller initially
        min_price = float('inf')  # smallest price seen so far (buy price)
        # Initialize max_profit to 0 because if no profit is possible, we must return 0
        max_profit = 0            # best profit so far
        
        # Iterate over each price once (one-pass)
        for price in prices:
            # Update min_price if we find a lower price (better day to buy)
            if price < min_price:
                min_price = price
            
            # Compute profit if we sell today after buying at min_price
            profit_today = price - min_price
            
            # Update max_profit if today's profit is better
            if profit_today > max_profit:
                max_profit = profit_today
        
        # Return the best profit found (or 0 if never improved)
        return max_profit


# CoderPad/HackerRank Test
from typing import List

def max_profit(prices: List[int]) -> int:
    # Edge case: if list is empty or has only one day -> cannot make profit
    if not prices or len(prices) < 2:
        return 0
    
    min_price = float('inf')  # track minimum price so far
    max_profit_value = 0      # track best profit found
    
    for price in prices:
        # update minimum price
        if price < min_price:
            min_price = price
        
        # compute profit if selling today
        profit_today = price - min_price
        
        # update max profit if it's better
        if profit_today > max_profit_value:
            max_profit_value = profit_today
    
    return max_profit_value


# Simple test cases
if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))  # Expected 5
    print(max_profit([7,6,4,3,1]))    # Expected 0
    print(max_profit([2,4,1]))        # Expected 2