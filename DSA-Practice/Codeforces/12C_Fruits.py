"""
Problem: Fruits
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/12/C
Difficulty: *1100
Date Solved: 2026-08-17
Topics: Greedy, Implementation, Sorting

Approach:
Each distinct fruit name must be assigned a distinct price from the
'prices' list (n prices, m purchases, n >= number of distinct fruits).
Count frequency of each fruit name, sort frequencies descending.
To minimize total cost: pair the most frequent fruit with the cheapest
price (sorted ascending), and so on down the line.
To maximize total cost: pair the most frequent fruit with the most
expensive price (sorted descending) instead.
This greedy pairing is optimal because swapping any two price
assignments between a higher-frequency and lower-frequency fruit
only worsens the objective (standard rearrangement inequality).

Time Complexity:  O(n log n + m) — dominated by sorting prices and
                   counting/sorting frequencies (at most n distinct).
Space Complexity: O(n + m) — for prices list, counts, and frequencies.
"""


# ------------------------- Solution -------------------------


from collections import Counter
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    prices = [int(x) for x in data[2 : 2 + n]]
    prices.sort()
    fruit_names = data[2 + n : 2 + n + m]
    counts = Counter(fruit_names)
    frequencies = sorted(counts.values(), reverse=True)
    min_price = sum(freq * price for freq, price in zip(frequencies, prices))
    max_price = sum(
        freq * price for freq, price in zip(frequencies, reversed(prices))
    )
    print(min_price, max_price)

if __name__ == "__main__":
    solve()
