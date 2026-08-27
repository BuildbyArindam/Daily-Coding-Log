"""
Problem: Illegible String
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/illegible-string/
Date: 2026-08-27
Difficulty: Easy
Topics: Approved, Implementation, Open

Approach:
    An illegible 'v'/'w' run can be reinterpreted as any combination of v's (1 unit)
    and w's (2 units) that sums to the same total "unit" count. So each maximal run
    of v/w characters is converted to a total unit count (v=1, w=2):
        - max_len for that run = using all v's -> unit count itself
        - min_len for that run = using as many w's as possible -> ceil(units / 2)
    Non-v/w characters always contribute exactly 1 to both min_len and max_len.
    Runs are flushed whenever a non-v/w character is hit, and once more after the loop.

Time complexity:  O(n) — single pass over the string
Space complexity: O(1) — only a few counters used
"""


# -------------------------- Solution ------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    s = input_data[1]
    min_len = 0
    max_len = 0
    current_v_units = 0
    for char in s:
        if char == 'v':
            current_v_units += 1
        elif char == 'w':
            current_v_units += 2
        else:
            if current_v_units > 0:
                min_len += (current_v_units + 1) // 2
                max_len += current_v_units
                current_v_units = 0
            min_len += 1
            max_len += 1
    if current_v_units > 0:
        min_len += (current_v_units + 1) // 2
        max_len += current_v_units
    print(f"{min_len} {max_len}")

if __name__ == '__main__':
    solve()
