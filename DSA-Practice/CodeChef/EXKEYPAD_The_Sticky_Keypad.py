"""
Platform   : CodeChef (Starters 261, Div 4/3 - START261A)
Problem    : The Sticky Keypad (EXKEYPAD)
Link       : https://www.codechef.com/START261A/problems/EXKEYPAD
Date       : 2026-10-21
Difficulty : Medium
Topics     : Math, Greedy, Simulation

Approach:
    Treat the number as a decimal string. If it contains the sticky digit d,
    take its leftmost occurrence, increment the prefix up to that position and
    zero out the tail (the smallest number > current that removes that
    occurrence). Repeat until no occurrence of d remains. Re-checking after
    each bump handles carries and d = 0, where the zeroed tail reintroduces d.

Complexity:
    Time  : O(L^2) per test (L = number of digits; O(L) bumps, each O(L) for
            string conversion and search)
    Space : O(L) per test, O(T) for buffered output
"""


# ----------------------------------------------- Solution -----------------------------------------------------------


import sys

def _rd():
    return sys.stdin.read().split()

def _emit(lines):
    sys.stdout.write("\n".join(lines) + "\n")

def _hit(s, ch):
    return s.find(ch)

def _bump(val, ch):
    txt = str(val)
    pos = _hit(txt, ch)
    if pos < 0:
        return val, False
    tail = len(txt) - pos - 1
    unit = 10 ** tail
    return (val // unit + 1) * unit, True

def _solve(n, d):
    ch = str(d)
    cur = n
    go = True
    while go:
        cur, go = _bump(cur, ch)
    return cur

def main():
    tok = _rd()
    cnt = int(tok[0])
    res = []
    p = 1
    for _ in range(cnt):
        a = int(tok[p])
        b = int(tok[p + 1])
        p += 2
        res.append(str(_solve(a, b)))
    _emit(res)

if __name__ == "__main__":
    main()
