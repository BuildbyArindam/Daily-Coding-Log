"""
Platform   : CodeChef
Problem    : Permutation Jumble (PERMJUMB)
Link       : https://www.codechef.com/problems/PERMJUMB
Date       : 2026-10-07
Difficulty : Hard
Topics     : Permutations, Cycle Decomposition, Sliding Window, Bit Manipulation

Approach:
  1. Compose the two permutations into q[i] = b[a[i]-1]-1 and split q into
     disjoint cycles with a visited array.
  2. Cycles whose length is a power of two are already good, so their value
     sums are added directly.
  3. For other cycles, let p be the largest power of two <= L:
       - if L - p is also a power of two, the whole cycle's sum is a candidate;
       - otherwise slide a circular window of size p over the cycle and keep
         the best window sum.
  4. Track the best sum per cycle length, then try pairing two cycles whose
     lengths add up to a power of two, and keep the best total gain.
  5. Answer = untouched power-of-two sum + best extra gain.

Complexity:
  Time  : O(n) per test for cycle decomposition and windows, plus
          O(D log n) for the pairing step (D = distinct cycle lengths)
  Space : O(n)
"""


# -------------------------------------------- Solution -----------------------------------------------------------


import sys

def solve_case(n, a, b):
    q = [b[a[i] - 1] - 1 for i in range(n)]
    seen = bytearray(n)
    untouched = 0         
    extra_from_split = 0   
    top = {}
    power_cycle = {}
    for start in range(n):
        if seen[start]:
            continue
        cyc = []
        u = start
        while not seen[u]:
            seen[u] = 1
            cyc.append(u + 1) 
            u = q[u]
        L = len(cyc)
        total = sum(cyc)
        old = top.get(L, 0)
        if total > old:
            top[L] = total
        is_pow = (L & (L - 1)) == 0
        power_cycle[L] = is_pow
        if is_pow:
            untouched += total
            continue
        p = 1 << (L.bit_length() - 1)
        other = L - p
        if other & (other - 1) == 0:
            if total > extra_from_split:
                extra_from_split = total
            continue
        window = sum(cyc[:p])
        best_window = window
        tail = cyc + cyc[:p - 1]
        for left in range(1, L):
            window += tail[left + p - 1] - tail[left - 1]
            if window > best_window:
                best_window = window
        if best_window > extra_from_split:
            extra_from_split = best_window
    answer = untouched + extra_from_split
    current_gain = answer - untouched
    for x in top:
        if power_cycle[x]:
            continue
        need_power = 1 << ((x + 1).bit_length() - 1)
        while need_power - x <= n:
            y = need_power - x
            if y >= 1 and y in top:
                gain = top[x]
                if not power_cycle[y]:
                    gain += top[y]
                if gain > current_gain:
                    current_gain = gain
            need_power <<= 1
    return untouched + current_gain

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    t = data[ptr]
    ptr += 1
    out = []
    for _ in range(t):
        n = data[ptr]
        ptr += 1
        a = data[ptr:ptr + n]
        ptr += n
        b = data[ptr:ptr + n]
        ptr += n
        out.append(str(solve_case(n, a, b)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
