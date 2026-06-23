# You are given an array prices where prices[i]
# is the price of a stock on day i.

# Choose one day to buy and a later day to sell.

# Return the maximum profit.

# If no profit is possible, return 0.

# prices = [7,1,5,3,6,4]
# output =5
# Buy on day 1 at price 1
# Sell on day 4 at price 6

# Profit = 6 - 1 = 5

prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    lowest_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < lowest_price:
            lowest_price = price
        else:
            profit = price - lowest_price

            if profit > max_profit:
                max_profit = profit

    return max_profit


print("Maximum Profit =", maxProfit(prices))