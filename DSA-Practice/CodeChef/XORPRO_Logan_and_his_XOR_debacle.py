"""
Problem   : Logan and his XOR debacle (XORPRO)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/XORPRO
Difficulty: 1816
Topics    : Bitwise XOR, Math, Implementation
Date      : 2026-10-13

Approach:
    Compute the XOR of the whole array (xor_sum). If it is 0, the answer is 0.
    Otherwise, for each element a, the XOR of all the other elements is
    xor_sum ^ a. The cost for that element is |a - (xor_sum ^ a)|, and the
    answer is the minimum cost over all elements.

Complexity:
    Time : O(N) per test case (two linear passes)
    Space: O(N) for the input array (O(1) extra)
"""


# ------------------------------------------------- Solution --------------------------------------------------------


def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        xor_sum = 0
        for num in arr:
            xor_sum ^= num
        if xor_sum == 0:
            print(0)
            continue
        ans = float('inf')
        for num in arr:
            target = xor_sum ^ num
            operations = abs(num - target)
            ans = min(ans, operations)
        print(ans)

if __name__ == "__main__":
    solve()
