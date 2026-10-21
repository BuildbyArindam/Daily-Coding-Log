"""
Problem   : Exun Photo (EXPHOTO)
Platform  : CodeChef - Starters 261 (START261A)
Link      : https://www.codechef.com/START261A/problems/EXPHOTO
Date      : 2026-10-21
Difficulty: Easy
Topics    : Fenwick Tree, Counting, Math 

Approach  :
  Process the array left to right with a Fenwick Tree (BIT) indexed by value.
  For each element v, query how many earlier elements are smaller than v
  (prefix sum up to v-1). If that count s is non-zero, add ceil(s / (k-1))
  to the answer, since each operation handles k-1 such elements.
  If k == 1 and s > 0, no operation can fix it, so the answer is -1.
  Then insert v into the BIT.

Time      : O(N log N) per test case
Space     : O(N) per test case
"""


# ----------------------------------------------- Solution -------------------------------------------------------------


import sys

def main():
    buf = sys.stdin.buffer.read().split()
    pos = 0
    tc = int(buf[pos]); pos += 1
    res = []
    while tc:
        tc -= 1
        n = int(buf[pos]); k = int(buf[pos + 1]); pos += 2
        arr = buf[pos:pos + n]; pos += n
        tree = [0] * (n + 1)
        step = k - 1
        total = 0
        impossible = False
        for raw in arr:
            v = int(raw)
            s = 0
            j = v - 1
            while j > 0:
                s += tree[j]
                j &= j - 1
            if s:
                if step == 0:
                    impossible = True
                    break
                total += (s + step - 1) // step
            j = v
            while j <= n:
                tree[j] += 1
                j += j & -j
        res.append(-1 if impossible else total)
    sys.stdout.write("\n".join(map(str, res)) + "\n")

main()
