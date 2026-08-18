"""
Problem: Chef and Groups (GROFR)
Link: https://www.codechef.com/problems/GROFR
Date solved: 2026-08-18
Difficulty: Easy (~1200, CodeChef 1-star)
Topics: Strings, Greedy/Simulation

Approach:
Scan the seat string left to right once. A new "group" starts every
time we see a '1' immediately preceded by a '0' (or by nothing, at
the very start). Track the previous character and increment a
counter only on these 0->1 transitions; consecutive 1's after that
are part of the same group and don't add to the count.

Time complexity:  O(n)  -- single pass over the string
Space complexity: O(1)  -- excluding input storage
"""


# --------------------- Solution ------------------------


import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    total_groups = 0
    prev_char = '0'
    idx = 0
    while idx < n:
        cur = s[idx]
        if cur == '1' and prev_char == '0':
            total_groups += 1
        prev_char = cur
        idx += 1
    print(total_groups)

if __name__ == "__main__":
    main()
