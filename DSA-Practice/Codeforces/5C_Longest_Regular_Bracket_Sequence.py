"""
Problem   : Longest Regular Bracket Sequence
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/5/C
Difficulty: *1900
Topics    : constructive algorithms, data structures, dp, greedy, sortings, strings
Date      : 2026-08-17

Approach:
    Maintain a stack of indices of "unmatched" characters, seeded with -1
    as a virtual boundary before the string. For each '(' push its index.
    For each ')':
        - pop the stack (attempt to match)
        - if the stack becomes empty, there's no unmatched '(' to pair
          with, so push i as the new boundary/base index
        - otherwise, the length of the regular sequence ending at i is
          i - stack[-1] (distance from the current unmatched base).
          Track the max length seen and how many times it's achieved.

Complexity:
    Time : O(n)  -- each index pushed/popped at most once
    Space: O(n)  -- worst case stack holds all '(' indices
"""


# -------------------- Solution --------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    stack = [-1]
    max_len = 0
    count = 1
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                length = i - stack[-1]
                if length > max_len:
                    max_len = length
                    count = 1
                elif length == max_len:
                    count += 1
    print(f"{max_len} {count}")

if __name__ == '__main__':
    solve()
