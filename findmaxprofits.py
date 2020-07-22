"""
returns the max profit that can be made with a single buy/sell
must buy before selling
if prices = [1050, 270, 1540, 3800, 2]
(the prices are in order, okay now it makes sense)
find_max_profit(prices) -> should be 3530


but why did it pick 3800 and 270? instead of 3800 and 2?
FIRST -  find the max,
SECOND - find the min up to the max

1. Run through examples, including your own

2. Ask questions to crreate a checklist of tasks to handle
"""

# THIS ITERATION DOESNT WORK FOR:
# [4999, 5000, 100, 2000] -> it returns 1 instead of 1900
# def find_max_profits(prices):
#     max_index = 1
#     max_price = prices[max_index]
#     for i in range(len(prices)):
#         if prices[i] >= max_price:
#             max_price = prices[i]
#             max_index = i
#     min_price = min(prices[:max_index])
#     return max_price - min_price


def find_max_profits(prices):
    max_index = 1
    max_price = prices[max_index]
    for i in range(len(prices) - 1):
        if prices[i + 1] >= max_price:
            max_price = prices[i + 1]
            max_index = i + 1
    min_price = min(prices[:max_index])
    max_profit = max_price - min_price
    for i in range(len(prices)):
        for j in range(len(prices[:-(i + 1)])):
            top_index = len(prices) - i - 1
            cur_profit = prices[top_index] - prices[j]
            if cur_profit > max_profit:
                max_profit = cur_profit
    return max_profit


p1 = [1050, 270, 1540, 3800, 2]
print(find_max_profits(p1))  # expect 3530
p2 = [1000, 900, 800, 700]
print(find_max_profits(p2))  # expect -100
p3 = [1050, 4000, 3455, 32, 0, 0, 1000]
print(find_max_profits(p3))
p4 = [4999, 5000, 100, 2000]
print(find_max_profits(p4))
