"""
Problem   : Mancunian And Fantabulous Pairs
Platform  : HackerEarth (Medium)
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/mancunian-and-fantabulous-pairs/
Date      : 2026-09-28
Topics    : Data Structures, Math, Stacks

Approach  : Monotonic (non-increasing) stack of indices. When element x at
            index j pops index i, j is the nearest strictly greater element
            to the right of i, and the new stack top p is the nearest
            element >= a[i] to its left. That gives distance = j - i and
            span = i - p. Keep the max span per distance in best[], then
            print sum(best).

Time      : O(n), since each index is pushed and popped at most once.
Space     : O(n) for the stack and the best[] array.
"""


# ---------------------------------- Solution ------------------------------------------


import sys
from array import array
data = sys.stdin.buffer.read().split()
n = int(data[0])
best = array('I', [0]) * (n + 1)
stack_i = array('I')
stack_v = array('I')
for j in range(1, n + 1):
    x = int(data[j])
    while stack_v and stack_v[-1] < x:
        i = stack_i.pop()
        stack_v.pop()
        p = stack_i[-1] if stack_i else 0
        distance = j - i
        span = i - p
        if span > best[distance]:
            best[distance] = span
    stack_i.append(j)
    stack_v.append(x)
print(sum(best))
