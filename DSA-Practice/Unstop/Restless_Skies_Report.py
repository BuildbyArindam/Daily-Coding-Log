"""
Problem   : Restless Skies Report
Platform  : Unstop 
Link      : http://unstop.com/code/practice/667563
Date      : 2026-10-26
Difficulty: Hard
Topics    : Monotonic Stack, Sparse Table, Prefix Sums, Offline Queries

Approach
--------
For each query [L, R], the answer is the sum over all subarrays inside [L, R]
of (max - min). It is computed as (sum of subarray maxima) + (sum of subarray
maxima of the negated array), since max(-a) = -min(a).

1. A monotonic stack gives each index's previous greater (left) and next
   greater-or-equal (right), which handles ties without double counting.
2. D[i] = sum of maxima of all subarrays ending at i, built as
   D[i] = a[i] * (i - left[i]) + D[left[i]]. PS is its prefix sum.
3. A1/A2 are suffix accumulators along the "next greater" chain, so the
   contribution of subarrays starting at L and crossing the chain up to the
   range maximum M can be evaluated in O(1).
4. A sparse table finds M = argmax in [L, R] in O(1). The final sum combines
   the PS difference, the chain terms, and the tail term from M to R.
5. Run once on the array and once on the negated array, add the results,
   then pick the first query with the largest value (1-based index).

Time  : O(n log n + q)  (sparse table build + O(1) per query)
Space : O(n log n)      (sparse table; everything else is O(n + q))
"""


# ----------------------------------------------- Solution ------------------------------------------------------------


import sys

def window_peak_sums(vals, qa, qb, n):
    left = [0] * (n + 2)
    st = []
    for i in range(1, n + 1):
        x = vals[i]
        while st and vals[st[-1]] < x:
            st.pop()
        left[i] = st[-1] if st else 0
        st.append(i)
    right = [n + 1] * (n + 2)
    st = []
    for i in range(n, 0, -1):
        x = vals[i]
        while st and vals[st[-1]] <= x:
            st.pop()
        right[i] = st[-1] if st else n + 1
        st.append(i)
    D = [0] * (n + 2)
    PS = [0] * (n + 2)
    for i in range(1, n + 1):
        D[i] = vals[i] * (i - left[i]) + D[left[i]]
        PS[i] = PS[i - 1] + D[i]
    A1 = [0] * (n + 3)
    A2 = [0] * (n + 3)
    for m in range(n, 0, -1):
        g = right[m]
        c = g - m
        A1[m] = (vals[m] * (m + 1) - D[m]) * c + A1[g]
        A2[m] = vals[m] * c + A2[g]
    tabs = [list(range(n + 1))]
    k = 1
    while (1 << k) <= n:
        prev = tabs[-1]
        h = 1 << (k - 1)
        tabs.append([i if vals[i] >= vals[j] else j
                     for i, j in zip(prev, prev[h:])])
        k += 1
    out = []
    for L, R in zip(qa, qb):
        t = (R - L + 1).bit_length() - 1
        tb = tabs[t]
        x = tb[L]
        y = tb[R - (1 << t) + 1]
        M = x if vals[x] >= vals[y] else y
        s = PS[R] - PS[L - 1] + A1[L] - A1[M] - L * (A2[L] - A2[M])
        s += (vals[M] * (M - L + 1) - D[M]) * (R - M + 1)
        out.append(s)
    return out

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    seq = [0] + [int(x) for x in data[1:1 + n]]
    q = int(data[1 + n])
    raw = list(map(int, data[2 + n:2 + n + 2 * q]))
    qa = raw[0::2]
    qb = raw[1::2]
    top = window_peak_sums(seq, qa, qb, n)
    neg = [0] + [-x for x in seq[1:]]
    bot = window_peak_sums(neg, qa, qb, n)
    res = [u + v for u, v in zip(top, bot)]
    best = 0
    for i in range(1, q):
        if res[i] > res[best]:
            best = i
    sys.stdout.write(" ".join(map(str, res)) + "\n")
    sys.stdout.write(str(best + 1) + "\n")

main()
