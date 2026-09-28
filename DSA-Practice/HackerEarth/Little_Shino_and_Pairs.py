"""
Problem   : Little Shino and Pairs
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/little-shino-and-pairs/
Difficulty: Easy
Topics    : Data Structures, Stacks
Date      : 2026-09-28

Approach  : Monotonic (non-increasing) stack, run in both directions.
            Scanning left to right, pop every element smaller than the
            current one, then if the stack is non-empty the current element
            forms one valid pair with the stack top. Scanning right to left
            catches the pairs the first pass misses. The stack is popped
            at most once per element.

Time      : O(N)
Space     : O(N)
"""


# ---------------------------------- Solution -------------------------------------------


n = int(input())
a = list(map(int, input().split()))
answer = 0
stack = []
for x in a:
    while stack and stack[-1] < x:
        stack.pop()
    if stack:
        answer += 1
    stack.append(x)
stack = []
for x in reversed(a):
    while stack and stack[-1] < x:
        stack.pop()
    if stack:
        answer += 1
    stack.append(x)
print(answer)
