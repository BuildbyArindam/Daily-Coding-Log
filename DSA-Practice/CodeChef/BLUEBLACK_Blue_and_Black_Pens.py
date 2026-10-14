"""
Problem   : Blue and Black Pens (BLUEBLACK)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BLUEBLACK
Date      : 2026-10-14
Difficulty: Easy
Topics    : Math, Implementation

Approach  : There are two ways to buy a set, so compute the cost of each
            and print the cheaper one.
              1. Triple option: 3 * blue_price
              2. Mixed option : black_price + blue_price
            The answer is min(triple, mixed).

Complexity: Time  O(1) - a constant number of arithmetic operations
            Space O(1) - only a few integer variables
"""


# --------------------------------------------- Solution ------------------------------------------------------------


def cheapest_set(blue_price, black_price):
    option_triple = blue_price + blue_price + blue_price
    option_mixed = black_price + blue_price
    if option_mixed < option_triple:
        return option_mixed
    return option_triple

def main():
    values = [int(token) for token in input().strip().split()]
    blue, black = values[0], values[1]
    print(cheapest_set(blue, black))

if __name__ == "__main__":
    main()
