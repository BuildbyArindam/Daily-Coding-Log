"""
Problem   : Beautiful Array (BTAR)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BTAR
Difficulty: 1800
Topics    : Modular Arithmetic, Mathematics
Date      : 2026-10-04

Approach:
    Only a[i] % 4 matters, so count residues 1, 2 and 3. If the total
    residue sum isn't divisible by 4, the answer is -1. Otherwise, greedily
    form the maximum number of disjoint groups whose residues sum to 0 mod 4,
    in this order: (1,3), (2,2), then (1,1,2) or (3,3,2) if a lone 2 is left,
    then leftover (1,1,1,1) or (3,3,3,3). A group of size k costs k-1
    operations, so the answer is (non-zero elements) - (groups).

Complexity:
    Time : O(n) per test case (single pass to count residues)
    Space: O(1) extra (four counters, apart from the input list)
"""


# --------------------------------------- Solution ----------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = [0, 0, 0, 0]
        for x in a:
            cnt[x % 4] += 1
        if (cnt[1] + 2 * cnt[2] + 3 * cnt[3]) % 4 != 0:
            print(-1)
            continue
        c1, c2, c3 = cnt[1], cnt[2], cnt[3]
        groups = min(c1, c3)
        c1 -= groups
        c3 -= groups
        groups += c2 // 2
        c2 %= 2
        if c1:
            if c2 == 1:
                groups += 1       
                c1 -= 2
            groups += c1 // 4
        elif c3:
            if c2 == 1:
                groups += 1       
                c3 -= 2
            groups += c3 // 4
        nonzero = cnt[1] + cnt[2] + cnt[3]
        answer = nonzero - groups
        print(answer)

if __name__ == "__main__":
    solve()
