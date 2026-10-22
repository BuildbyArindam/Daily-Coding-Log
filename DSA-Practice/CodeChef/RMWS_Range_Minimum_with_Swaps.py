"""
Platform   : CodeChef
Problem    : Range Minimum with Swaps (RMWS)
Link       : https://www.codechef.com/problems/RMWS
Difficulty : 2050
Date       : 2026-10-22
Topics     : Segment Tree, Point Update, Range Minimum Query

Approach:
    Build an iterative (bottom-up) segment tree over the array, storing the
    minimum of each range. A swap of positions u and v exchanges the two leaf
    values and then recomputes the ancestors of both leaves. A range-minimum
    query walks the tree bottom-up, taking the minimum over the O(log n)
    nodes that cover [l, r].

Complexity:
    Time  : O(n + q log n)  (O(n) build, O(log n) per swap or query)
    Space : O(n)            (tree array of size 2 * next_pow2(n))
"""


# -------------------------------------------- Solution ---------------------------------------------------------


import sys

def build_tree(vals, size, big):
    tree = [big] * (2 * size)
    for idx, v in enumerate(vals):
        tree[size + idx] = v
    for k in range(size - 1, 0, -1):
        left, right = tree[k << 1], tree[k << 1 | 1]
        tree[k] = left if left < right else right
    return tree

def refresh(tree, pos):
    pos >>= 1
    while pos:
        left, right = tree[pos << 1], tree[pos << 1 | 1]
        tree[pos] = left if left < right else right
        pos >>= 1

def query(tree, size, big, lo, hi):
    a = lo - 1 + size
    b = hi + size
    best = big
    while a < b:
        if a & 1:
            if tree[a] < best:
                best = tree[a]
            a += 1
        if b & 1:
            b -= 1
            if tree[b] < best:
                best = tree[b]
        a >>= 1
        b >>= 1
    return best

def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    values = list(map(int, tokens[1:1 + n]))
    q = int(tokens[1 + n])
    size = 1
    while size < n:
        size <<= 1
    big = 1 << 62
    tree = build_tree(values, size, big)
    answers = []
    ptr = 2 + n
    for _ in range(q):
        kind = tokens[ptr]
        u = int(tokens[ptr + 1])
        v = int(tokens[ptr + 2])
        ptr += 3
        if kind == b'2':
            answers.append(query(tree, size, big, u, v))
        elif u != v:
            pu = u - 1 + size
            pv = v - 1 + size
            tree[pu], tree[pv] = tree[pv], tree[pu]
            refresh(tree, pu)
            refresh(tree, pv)
    sys.stdout.write("\n".join(map(str, answers)))
    if answers:
        sys.stdout.write("\n")

main()
