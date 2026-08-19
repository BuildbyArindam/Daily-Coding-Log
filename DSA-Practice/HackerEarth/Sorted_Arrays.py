"""
Problem   : Sorted Arrays (Killjee and Sorted Array)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/killjee-and-sorted-array-ae92a57f/
Difficulty: Easy
Topics    : Arrays, Basic Programming, Greedy
Date      : 2026-08-19

Approach:
    Greedy left-to-right scan. Maintain the invariant that a[i-1] < a[i]
    after processing index i. Whenever a[i] <= a[i-1], bump a[i] up to
    a[i-1] + 1, adding the difference to the move counter. Since each
    element only needs to exceed its immediate predecessor, this greedy
    choice is optimal — bumping any less would violate strict order
    later, and bumping more would waste moves.

Time Complexity : O(n)  -- single pass over the array
Space Complexity: O(1)  -- modifies array in place, no extra structures
"""


# --------------------------- Solution ----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = list(map(int, input_data[1:n + 1]))
    moves = 0
    for i in range(1, n):
        if a[i] <= a[i - 1]:
            target = a[i - 1] + 1
            moves += target - a[i]
            a[i] = target
    print(moves)

if __name__ == '__main__':
    solve()
