"""
Problem   : List of Books (BOOKLIST)
Platform  : CodeChef (ZCO/INOI practice, IARCSJUD)
Link      : https://www.codechef.com/practice/course/zco-inoi-problems/IARCSJUD/problems/BOOKLIST
Date      : 2026-10-21
Difficulty: Hard
Topics    : Fenwick Tree (BIT), Binary Lifting, Order Statistics

Approach:
    Each query asks for the k-th book currently on the shelf, which is then
    removed. This is a dynamic k-th element problem.
    - Keep a Fenwick tree over positions, where 1 means "book still present".
      The tree starts with every position set to 1, so bit[i] = i & -i,
      which builds it in O(N) with no update loop.
    - To find the k-th remaining book, binary-lift down the tree from the
      highest power of two, skipping blocks whose count is < k. This lands on
      the position of the k-th present book in O(log N).
    - Output that title, then decrement 1 along its update path.

Time  : O(N + Q log N)
Space : O(N)
"""


# ------------------------------------------------- Solution ------------------------------------------------------


import sys

def main():
    data = sys.stdin.buffer.read().split()
    total = int(data[0])
    shelf = data[1:1 + total]
    q = int(data[1 + total])
    asks = data[2 + total:2 + total + q]
    bit = [i & -i for i in range(total + 1)]
    top = 1
    while top * 2 <= total:
        top *= 2
    out = []
    for a in asks:
        need = int(a)
        pos = 0
        step = top
        while step:
            nxt = pos + step
            if nxt <= total and bit[nxt] < need:
                pos = nxt
                need -= bit[nxt]
            step >>= 1
        pos += 1
        out.append(shelf[pos - 1].decode())
        j = pos
        while j <= total:         
            bit[j] -= 1
            j += j & -j
    sys.stdout.write("\n".join(out) + "\n")

main()
