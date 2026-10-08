"""
Problem   : And Or Union
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ANDORUNI
Difficulty: 1728
Topics    : Bit Manipulation
Date      : 2026-10-08

Approach:
    Count how many array elements have each bit set (bits 0-29).
    A bit goes into the answer only if at least 2 elements have it set.
    Build the answer by OR-ing in 1 << bit for each qualifying bit.

Complexity:
    Time  : O(30 * N) per test case
    Space : O(30) = O(1) extra, apart from the input array
"""


# ------------------------------------- Solution ----------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        cnt = [0] * 30
        for x in A:
            for bit in range(30):
                if x & (1 << bit):
                    cnt[bit] += 1
        ans = 0
        for bit in range(30):
            if cnt[bit] >= 2:
                ans |= (1 << bit)
        print(ans)

if __name__ == "__main__":
    solve()
