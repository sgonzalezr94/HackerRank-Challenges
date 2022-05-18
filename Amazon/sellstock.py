# Array of prices which holds stock value on the i`th day.
# prices = [7,1,5,3,6,4]
# We want to maximize the value on the stock sell
from typing import List


testprices = [7, 1, 5, 3, 6, 4]
testprices2 = [7, 6, 4, 3, 1]

# O(n2) non optimal solution
# def maxProfit(prices: List[int]) -> int:
#     profit = 0
#     i = 0
#     while i < len(prices):
#         j = 0
#         while j < len(prices[i + 1 :]):
#             calculated_profit = prices[i + j + 1] - prices[i]
#             if calculated_profit > profit:
#                 profit = calculated_profit
#             j += 1
#         i += 1
#     return profit

# O(n) solution
def maxProfit(prices: List[int]) -> int:
    i = min_idx = 0
    min = prices[0]
    profit = 0
    while i < len(prices):
        if prices[i] < min:
            min = prices[i]
            min_idx = i
        if prices[i] - prices[min_idx] > profit:
            profit = prices[i] - prices[min_idx]
        i += 1
    return profit


final_profit = maxProfit(testprices)
print(final_profit)
