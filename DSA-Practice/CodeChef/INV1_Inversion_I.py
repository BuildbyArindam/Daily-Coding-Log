# Problem   : Inversion I
# Platform  : CodeChef
# Link      : https://www.codechef.com/problems/INV1
# Date      : 2026-09-04
# Difficulty: Hard
# Topics    : Segment Tree (Range Assign / Range Min / Range Sum), Monotonic Stack, Lazy Propagation
#
# Approach:
#   Process array left to right while maintaining a monotonic (non-increasing)
#   stack of "active" positions on a segment tree that supports:
#     - range assign (set a contiguous range to value x)
#     - range sum query
#     - range min query (to binary search the first position with value < x)
#   When a new element x arrives, pop all stack elements <= x (they get
#   absorbed into a merged block), combine the top of the stack's value with
#   x, then range-assign that merged value back onto the segment tree from
#   the first position (found via first_less) up to the popped position.
#   The running sum sm[1] after each insertion gives the contribution for
#   that prefix, accumulated into the answer.
#
# Time complexity : O(n log n) — each element pushed/popped from the stack
#                    once (amortized), each segment tree op is O(log n).
# Space complexity: O(n) — segment tree arrays sized 4n.


# ------------------------- Solution ----------------------------------


import sys

def solve(A):
    n = len(A)
    size = 4 * n + 5
    sm = [0] * size
    mn = [0] * size
    lazy = [-1] * size
    def apply(v, l, r, x):
        sm[v] = (r - l + 1) * x
        mn[v] = x
        lazy[v] = x
    def push(v, l, r):
        x = lazy[v]
        if x == -1 or l == r:
            return
        m = (l + r) >> 1
        lc = v << 1
        rc = lc | 1
        apply(lc, l, m, x)
        apply(rc, m + 1, r, x)
        lazy[v] = -1
    def first_less(v, l, r, p, x):
        if l > p or mn[v] >= x:
            return p + 1
        if l == r:
            return l
        push(v, l, r)
        m = (l + r) >> 1
        res = first_less(v << 1, l, m, p, x)
        if res <= p:
            return res
        return first_less(v << 1 | 1, m + 1, r, p, x)
    def assign(v, l, r, ql, qr, x):
        if ql <= l and r <= qr:
            apply(v, l, r, x)
            return
        push(v, l, r)
        m = (l + r) >> 1
        lc = v << 1
        rc = lc | 1
        if ql <= m:
            assign(lc, l, m, ql, qr, x)
        if qr > m:
            assign(rc, m + 1, r, ql, qr, x)
        sm[v] = sm[lc] + sm[rc]
        mn[v] = mn[rc]
    stack = []
    ans = 0
    for r in range(1, n + 1):
        x = A[r - 1]
        while stack and A[stack[-1] - 1] <= x:
            stack.pop()
        if stack:
            p = stack[-1]            
            new_value = A[p - 1] + x
            q = first_less(1, 1, n, p, new_value)
            if q <= p:
                assign(1, 1, n, q, p, new_value)
        stack.append(r)
        ans += sm[1]
    return ans

def main():
    input = sys.stdin.buffer.readline
    T = int(input())
    out = []
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))
        out.append(str(solve(A)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
