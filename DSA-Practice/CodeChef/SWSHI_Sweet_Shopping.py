# Problem   : Sweet Shopping (SWSHI)
# Platform  : CodeChef
# Link      : https://www.codechef.com/problems/SWSHI
# Date      : 2026-10-12
# Difficulty: Hard
# Topics    : Sliding Window, Two Pointers, Arrays
#
# Approach  : Sliding window over the prices array. Extend the right end
#             (hi) one item at a time, adding its cost to the running sum.
#             While the sum exceeds the budget, shrink from the left (lo).
#             After each step, the window [lo, hi] is the longest affordable
#             contiguous segment ending at hi; track the maximum length.
#             Relies on prices being non-negative, so shrinking never
#             increases the sum.
#
# Time      : O(N) per test case (each index enters and leaves the window once)
# Space     : O(N) to store prices, O(1) extra beyond that


# ----------------------------------------------- Solution ---------------------------------------------------


import sys

def longest_affordable(prices, budget):
    lo = 0
    spent = 0
    top = 0
    for hi, cost in enumerate(prices):
        spent += cost
        while spent > budget:
            spent -= prices[lo]
            lo += 1
        span = hi - lo + 1
        if span > top:
            top = span
    return top

def solve_all(tokens):
    ptr = 0
    cases = int(tokens[ptr])
    ptr += 1
    results = []
    for _ in range(cases):
        count = int(tokens[ptr])
        budget = int(tokens[ptr + 1])
        ptr += 2
        prices = list(map(int, tokens[ptr:ptr + count]))
        ptr += count
        results.append(longest_affordable(prices, budget))
    return results

def main():
    tokens = sys.stdin.buffer.read().split()
    sys.stdout.write("\n".join(map(str, solve_all(tokens))) + "\n")

if __name__ == "__main__":
    main()
