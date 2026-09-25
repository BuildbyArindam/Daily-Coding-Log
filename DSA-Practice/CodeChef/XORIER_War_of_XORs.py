# Problem: War of XORs (XORIER)
# Platform: CodeChef | Link: https://www.codechef.com/problems/XORIER
# Date: 2026-09-25 | Difficulty: 1713
# Topics: Bitwise XOR, Hashing/Frequency Counting, Combinatorics
#
# Approach:
#   Count pairs (i, j) with i < j where A[i] and A[j] share the same parity
#   (since same-parity pairs always XOR to an even number), then subtract
#   pairs whose XOR is exactly 0 (equal elements) or exactly 2 (differ only
#   in bit 1), since those are excluded from the valid count. Uses a running
#   frequency map so each element only needs to look back at elements seen
#   so far — no nested loop.
#
# Time Complexity:  O(N) per test case (single pass, O(1) hashmap ops)
# Space Complexity: O(N) per test case (frequency dict, worst case all distinct)


# --------------------------------- Solution ---------------------------------------


import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        even = 0
        odd = 0
        freq = defaultdict(int)
        bad_xor_0 = 0
        bad_xor_2 = 0
        for x in A:
            if x & 1:
                odd += 1
            else:
                even += 1
            bad_xor_0 += freq[x]
            bad_xor_2 += freq[x ^ 2]
            freq[x] += 1
        ans = even * (even - 1) // 2
        ans += odd * (odd - 1) // 2
        ans -= bad_xor_0
        ans -= bad_xor_2
        print(ans)

if __name__ == "__main__":
    solve()
