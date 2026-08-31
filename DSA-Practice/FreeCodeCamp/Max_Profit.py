"""
Problem   : Max Profit
Platform  : FreeCodeCamp — Daily Coding Challenge
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/07-02
Solved on : 2026-08-31
Difficulty: Easy-Medium
Topics: Arrays, Greedy, Two Pointers, Math

Approach:
  Single left-to-right scan tracking the minimum price seen so far.
  At each price greater than the running min, compute how many whole
  shares the budget can buy at that min price, then check if selling
  at the current price beats the best profit found so far. Uses
  Decimal throughout to avoid float rounding errors on currency math,
  and truncates (ROUND_DOWN) the final profit to 2 decimal places.

Time complexity  : O(n) — one pass over prices
Space complexity : O(n) — for the Decimal-converted price list
                   (O(1) extra if you convert in place / on the fly)
"""


# ------------------------ Solution ----------------------------


from decimal import Decimal, ROUND_DOWN

def get_max_profit(prices, budget):
    budget = Decimal(str(budget))
    prices = [Decimal(str(price)) for price in prices]
    max_profit = Decimal("0")
    min_price = None
    for price in prices:
        if min_price is None or price < min_price:
            min_price = price
            continue
        shares = int(budget // min_price)
        if shares > 0:
            profit = shares * (price - min_price)
            if profit > max_profit:
                max_profit = profit
    max_profit = max_profit.quantize(
        Decimal("0.01"),
        rounding=ROUND_DOWN
    )
    return f"{max_profit:.2f}"
