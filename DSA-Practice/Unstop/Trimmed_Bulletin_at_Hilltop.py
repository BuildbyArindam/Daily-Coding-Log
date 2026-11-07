"""
Problem   : Trimmed Bulletin at Hilltop
Platform  : Unstop
Link      : https://unstop.com/code/practice/670544
Difficulty: Hard
Date      : 2026-11-07
Topics    : Fenwick Tree (BIT), Coordinate Compression, Sliding Window,
            Two Pointers, Prefix Sum, Sorting

Approach
--------
- Readings and queries are both processed in time order, so the active
  window (now - W, now] is kept with two pointers: `hi` adds readings with
  time <= now, `lo` evicts readings with time <= now - W.
- Values are coordinate-compressed, and two Fenwick trees are maintained
  over the compressed values: one for counts and one for sums.
- For m active readings, k = floor(m * p / 100) are trimmed from each end.
  A binary-descent walk on the Fenwick tree finds the r-th smallest value
  and the sum of the r smallest values in O(log n). The answer uses:
    * kept count   = m - 2k
    * kept sum     = (sum of the smallest m-k) - (sum of the smallest k)
    * min kept     = (k+1)-th smallest
    * max kept     = (m-k)-th smallest
- If the window is empty, print "NO DATA".

Assumptions: readings are sorted by time and queries by non-decreasing
time (required by the two-pointer sweep).

Complexity
----------
Time : O((n + q) log n)  -- each reading is added and removed once, and
                            each query does O(1) Fenwick walks
Space: O(n + q)
"""


# ------------------------------------------------------ Solution ------------------------------------------------------------------


import sys

def main():
    tok = sys.stdin.buffer.read().split()
    n = int(tok[0]); q = int(tok[1]); W = int(tok[2])
    base = 3
    rt = [0] * n  
    rv = [0] * n        
    for i in range(n):
        rt[i] = int(tok[base + 2 * i])
        rv[i] = int(tok[base + 2 * i + 1])
    base += 2 * n
    bt = [0] * q      
    bp = [0] * q        
    for j in range(q):
        bt[j] = int(tok[base + 2 * j])
        bp[j] = int(tok[base + 2 * j + 1])
    vals = sorted(set(rv))
    sz = len(vals)
    where = {x: i + 1 for i, x in enumerate(vals)}
    slot = [where[x] for x in rv]
    top = 1
    while top * 2 <= sz:
        top *= 2
    fc = [0] * (sz + 1) 
    fs = [0] * (sz + 1)
    def bump(pos, dc, dv):
        while pos <= sz:
            fc[pos] += dc
            fs[pos] += dv
            pos += pos & (-pos)
    def smallest(r):
        at = 0
        gc = 0
        gs = 0
        st = top
        while st:
            nx = at + st
            if nx <= sz and gc + fc[nx] < r:
                at = nx
                gc += fc[nx]
                gs += fs[nx]
            st >>= 1
        v = vals[at]
        return v, gs + (r - gc) * v
    out = []
    hi = 0 
    lo = 0 
    for j in range(q):
        now = bt[j]
        while hi < n and rt[hi] <= now:
            bump(slot[hi], 1, rv[hi])
            hi += 1
        limit = now - W
        while lo < hi and rt[lo] <= limit:
            bump(slot[lo], -1, -rv[lo])
            lo += 1
        m = hi - lo
        if m == 0:
            out.append("NO DATA")
            continue
        k = (m * bp[j]) // 100
        right = m - k
        top_v, top_s = smallest(right)
        if k:
            _, low_s = smallest(k)
        else:
            low_s = 0
        low_v, _ = smallest(k + 1)
        out.append("%d %d %d %d" % (right - k, top_s - low_s, low_v, top_v))
    sys.stdout.write("\n".join(out) + "\n")

main()
