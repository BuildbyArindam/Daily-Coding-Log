"""
Problem   : Chocolate Stack
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/chocolate-stack-746c1b56/
Difficulty: Easy
Topics    : Basics of Stacks, Data Structures, Stacks
Date      : 2026-09-28

Approach:
    Simulate the pile with a stack (LIFO). Iterate through the events:
      - A positive value is a chocolate being placed on top -> push.
      - A 0 means take the top chocolate -> pop and record its value.
    The recorded values, in order, are the answer.

Complexity:
    Time  : O(N), one pass and O(1) per push/pop
    Space : O(N), stack plus result list in the worst case
"""


# -------------------------------------- Solution ---------------------------------------------


def solution (N, C):
    stack = []
    result = []
    for x in C:
        if x == 0:
            result.append(stack.pop())
        else:
            stack.append(x)
    return result
N = int(input())
C = list(map(int, input().split()))

out_ = solution(N, C)
print (' '.join(map(str, out_)))
