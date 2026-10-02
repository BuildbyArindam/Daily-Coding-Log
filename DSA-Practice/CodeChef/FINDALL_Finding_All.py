"""
Problem   : Finding All (FINDALL)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FINDALL
Difficulty: 1721
Topics    : Casework, Counting
Date      : 2026-10-02

Approach:
    Only the counts of -1 and +1 in the array matter, so count each once.
    The set of achievable values (-1, 0, 1) is then decided by case analysis:
      - both signs present -> 0 is achievable
      - -1 is also achievable if there are at least two 1s
      - 1 is also achievable if there are at least two -1s
      - only one sign present -> that sign is the only answer
      - neither present -> only 0
    Answers are printed in ascending order.

Time Complexity : O(N) per test case (two passes via list.count)
Space Complexity: O(N) for the input array, O(1) extra
"""


# ------------------------------------- Solution ------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        neg = A.count(-1)
        pos = A.count(1)
        ans = []
        if pos > 0 and neg > 0 and pos >= 2:
            ans.append(-1)
        if neg > 0 and pos > 0:
            ans.append(0)
        if neg >= 2 and pos > 0:
            ans.append(1)
        if neg > 0 and pos == 0:
            ans = [1]
        elif pos > 0 and neg == 0:
            ans = [-1]
        elif neg == 0 and pos == 0:
            ans = [0]
        print(*ans)

if __name__ == "__main__":
    solve()
