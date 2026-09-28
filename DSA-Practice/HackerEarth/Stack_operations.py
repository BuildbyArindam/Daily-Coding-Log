"""
Problem   : Stack operations
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/stakth-1-e6a76632/
Difficulty: Easy
Topics    : Arrays, Basic Programming, Data Structures, Implementation, Stacks
Date      : 2026-09-28

Approach:
    Treat the array as a stack and maximise the top element after exactly K moves
    (each move pops the top or pushes back a removed element). By case:
      - N == 1: the only element is popped and pushed back, so K odd -> -1 (empty), K even -> x.
      - K > N : every element can be exposed, so the answer is the max of all N.
      - K == N: the K-th element can't be the final top (the last move would have to push
                back the element just popped), so the answer is max of the first N-1.
      - K < N : the answer is max(first K-1 elements, element at index K).
    Input is parsed with a byte-level generator, and reading stops early once index K is seen.

Complexity:
    Time  : O(N), a single pass with early exit
    Space : O(N) for the raw input buffer, O(1) extra
"""


# ------------------------------------- Solution ------------------------------------------------


import sys

def integers():
    data = sys.stdin.buffer.read()
    num = 0
    in_num = False
    for b in data:
        if 48 <= b <= 57:
            num = num * 10 + (b - 48)
            in_num = True
        elif in_num:
            yield num
            num = 0
            in_num = False
    if in_num:
        yield num
it = integers()
N = next(it)
K = next(it)
if N == 1:
    x = next(it)
    if K % 2 == 1:
        print(-1)
    else:
        print(x)
    sys.exit(0)
if K > N:
    ans = 0
    for _ in range(N):
        x = next(it)
        if x > ans:
            ans = x
    print(ans)
    sys.exit(0)
if K == N:
    ans = 0
    for i in range(N):
        x = next(it)
        if i < N - 1 and x > ans:
            ans = x
    print(ans)
    sys.exit(0)
ans = 0
for i in range(N):
    x = next(it)
    if i < K - 1:
        if x > ans:
            ans = x
    elif i == K:
        if x > ans:
            ans = x
        break
print(ans)
