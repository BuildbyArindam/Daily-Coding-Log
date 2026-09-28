"""
Problem   : Minimum String Weight (MSTRW)
Platform  : CodeChef
Link      : https://www.codechef.com/DSAMONDAY022/problems/MSTRW
Date      : 2026-09-28
Difficulty: Medium
Topics    : Greedy, Strings, Frequency Count

Approach  : Greedy. The weight is the sum of squared character frequencies,
            so each removal should hit the currently most frequent character,
            since that reduces the sum the most. Count frequencies once, then
            decrement the max bucket K times.

Complexity: Time  - O(N + 26*K), one pass to count plus a 26-bucket scan per removal
            Space - O(1), a fixed 26-slot frequency array
"""


# -------------------------------- Solution -------------------------------------------------


import sys

def solve():
    raw = sys.stdin.read().split("\n")
    text = raw[0].strip() if raw else ""
    rest = [ln.strip() for ln in raw[1:] if ln.strip()]
    removals = int(rest[0]) if rest else 0
    slots = [0] * 26
    for c in text:
        slots[ord(c) - 97] += 1
    while removals:
        top = max(range(26), key=slots.__getitem__)
        slots[top] -= 1
        removals -= 1
    print(sum(v * v for v in slots))

if __name__ == "__main__":
    solve()
