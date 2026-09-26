"""
Problem   : Killer Monsters
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/killer-monsters-0b5cb283/
Date      : 2026-09-26
Difficulty: Easy
Topics    : Stacks, Sets, Data Structures

Approach:
    For each new monster's strength x, pop all monsters currently on the
    stack whose strength is <= x (they get killed by x). Push x onto the
    stack. The stack size after processing index i is the answer for that
    position, since it represents the monsters that "survive" so far,
    maintained as a strictly decreasing sequence.

Complexity:
    Time  : O(n) per test case (amortized — each element is pushed once
            and popped at most once across the whole array).
    Space : O(n) worst case for the stack (strictly decreasing input).
"""


# ------------------------------------- Solution --------------------------------------------


import sys
from array import array
from io import StringIO

def int_stream():
    for line in sys.stdin.buffer:
        for x in line.split():
            yield int(x)

def solve():
    it = int_stream()
    t = next(it)
    out = sys.stdout
    for _ in range(t):
        n = next(it)
        stack = array('H')
        ans = StringIO()
        for i in range(n):
            x = next(it)
            while stack and stack[-1] <= x:
                stack.pop()
            stack.append(x)
            if i:
                ans.write(' ')
            ans.write(str(len(stack)))
        ans.write('\n')
        out.write(ans.getvalue())

if __name__ == "__main__":
    solve()
