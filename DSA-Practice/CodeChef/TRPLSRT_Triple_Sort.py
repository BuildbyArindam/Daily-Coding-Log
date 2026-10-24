"""
Problem   : Triple Sort (TRPLSRT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/TRPLSRT
Difficulty: 2012
Date      : 2026-10-24
Topics    : Permutations, Cycle Decomposition, Constructive, Greedy

Approach:
  Decompose the permutation into cycles. Each 3-element rotation on a
  cycle of length >= 3 fixes two elements, so a cycle shrinks by 2 per move.
  Cycles of length 2 can't be fixed alone, so they are paired up: two
  2-cycles (p,q), (x,y) are resolved with 2 moves (p,q,x), (p,y,x).
  If the number of 2-cycles is odd, or total moves exceed the limit, print -1.

Complexity:
  Time : O(N) per test case, since each element is fixed once
  Space: O(N) for the array and the move list
"""


# ---------------------------------------------- Solution ---------------------------------------------------------


import sys

def solve_case(n, lim, arr):
    a = [0] + arr
    moves = []
    twos = []
    for st in range(1, n + 1):
        while a[st] != st:
            m = a[st]
            r = a[m]
            if r == st:
                twos.append((st, m))
                a[st] = st
                a[m] = m
                break
            moves.append((st, m, r))
            a[m], a[r], a[st] = a[st], a[m], a[r]
    if len(twos) & 1:
        return None
    for z in range(0, len(twos), 2):
        (p, q), (x, y) = twos[z], twos[z + 1]
        moves.append((p, q, x))
        moves.append((p, y, x))
    if len(moves) > lim:
        return None
    return moves

def main():
    tok = sys.stdin.buffer.read().split()
    cases = int(tok[0])
    cur = 1
    res = []
    for _ in range(cases):
        n = int(tok[cur]); lim = int(tok[cur + 1])
        cur += 2
        arr = list(map(int, tok[cur:cur + n]))
        cur += n
        got = solve_case(n, lim, arr)
        if got is None:
            res.append("-1")
        else:
            res.append(str(len(got)))
            res.extend("%d %d %d" % mv for mv in got)
    sys.stdout.write("\n".join(res) + "\n")

main()
