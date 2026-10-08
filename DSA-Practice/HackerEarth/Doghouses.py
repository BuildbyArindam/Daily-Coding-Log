"""
Problem   : Doghouses
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/doghouses/
Difficulty: Medium
Date      : 2026-10-08
Topics    : Bitmask, Frequency Counting, Brute Force (Subarray Sweep)

Approach:
    Fix every left endpoint and extend the right endpoint one step at a time,
    keeping a running frequency count of each Y value in the window.
    The values are also grouped by frequency using big-int bitsets:
      - active[f]  : bitset of Y values that occur exactly f times
      - present    : bitset of the frequencies that currently exist
    The highest and second-highest frequencies come from bit_length() on
    `present`. For the endpoint-dependent cases, masks (below[y], above[y])
    are ANDed with active[f] to find the best frequency among Y values
    strictly below or above a given endpoint's Y. The best candidate for
    each window is folded into a global maximum.

Complexity:
    Time  : O(N^2 * k), where k is the number of frequency levels scanned in
            get_below/get_above (small in practice). Each bitset operation
            costs O(MAX_Y / word_size).
    Space : O(N + MAX_Y) per left endpoint for freq/active, plus
            O(MAX_Y^2 / word_size) for the precomputed below/above masks.
"""


# --------------------------------------- Solution --------------------------------------------------


N = int(input())
Y = list(map(int, input().split()))

MAX_Y = 1000
FULL = (1 << (MAX_Y + 1)) - 1
below = [0] * (MAX_Y + 1)
above = [0] * (MAX_Y + 1)
for y in range(MAX_Y + 1):
    below[y] = (1 << y) - 1
    above[y] = FULL ^ ((1 << (y + 1)) - 1)
answer = 1
for left in range(N):
    freq = [0] * (MAX_Y + 1)
    active = [0] * (N + 1)
    present = 0
    yl = Y[left]
    for right in range(left, N):
        y = Y[right]
        old = freq[y]
        new = old + 1
        bit = 1 << y
        if old:
            active[old] ^= bit
            if active[old] == 0:
                present ^= 1 << old
        freq[y] = new
        active[new] |= bit
        if active[new] == bit:
            present |= 1 << new
        if left == right:
            continue
        yr = Y[right]
        max_freq = present.bit_length() - 1
        bits = active[max_freq]
        if bits & (bits - 1):
            second_freq = max_freq
        else:
            rest = present ^ (1 << max_freq)
            second_freq = rest.bit_length() - 1 if rest else 0
        best_here = max_freq + second_freq
        def get_below(y_limit):
            p = present
            mask = below[y_limit]
            while p:
                f = p.bit_length() - 1
                if active[f] & mask:
                    return f
                p ^= 1 << f
            return 0
        def get_above(y_limit):
            p = present
            mask = above[y_limit]
            while p:
                f = p.bit_length() - 1
                if active[f] & mask:
                    return f
                p ^= 1 << f
            return 0
        if yl < yr:
            b = get_below(yl)
            a = get_above(yr)
            best_here = max(
                best_here,
                1 + freq[yr] + b
            )
            best_here = max(
                best_here,
                1 + freq[yl] + a
            )
            best_here = max(
                best_here,
                2 + b + a
            )
        elif yl > yr:
            b = get_below(yr)
            a = get_above(yl)
            best_here = max(
                best_here,
                1 + freq[yr] + a
            )
            best_here = max(
                best_here,
                1 + freq[yl] + b
            )
            best_here = max(
                best_here,
                2 + b + a
            )
        else:
            b = get_below(yl)
            a = get_above(yl)
            best_here = max(
                best_here,
                2 + b + a
            )
        answer = max(answer, best_here)
print(answer)
