#!/usr/bin/python
import argparse

# Write a function `find_max_profit` that receives as input a list of stock prices. 
# Your function should return the maximum profit that can be made from a single buy and sell. 
# You must buy first before selling; no shorting is allowed here.

# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, 
# example 2 - find_max_profit([10, 7, 5, 8, 11, 9]) should return 6
# which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

# Hint
# For this problem, we essentially want to find the 
# maximum difference between the smallest and largest prices in the list of prices, 
# but we also have to make sure that the max profit is computed by subtracting some price by another price 
# that comes _before_ it; it can't come after it in the list of prices. 

def find_max_profit(prices):
  # find smallest price
  # find largest price
  # find difference between largets and smallest (largets - smallest)
  
#     prices.sort()
#     smallest_price = prices[0]
#     largest_price = prices[len(prices) - 1]
#     difference = largest_price - smallest_price

#     print('smallest price is:', smallest_price)
#     print('largest price is:', largest_price)
#     print('difference:', difference)
# find_max_profit([1050, 270, 1540, 3800, 2])

    maxprofit = 0
    current_price = prices[0]
    current_profit = 0
    lowest_price = prices[0]

    for i in range(1, len(prices) - 1):
        current_price = prices[i]
        if current_price < lowest_price:
            lowest_price = current_price
        current_profit = prices[i] - lowest_price

        if current_profit > maxprofit:
            maxprofit = current_profit
    return maxprofit

print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))