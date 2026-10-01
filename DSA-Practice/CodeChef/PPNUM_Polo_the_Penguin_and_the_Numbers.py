"""
Problem   : Polo the Penguin and the Numbers (PPNUM)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/PPNUM
Difficulty: 1718
Topics    : Modular Arithmetic, Math, Constructive, Ad-hoc
Date      : 2026-10-01

Approach:
    For each query [L, R], the answer is the sum of i * digits(i) over the range.
    Using prefix sums, answer = F(R) - F(L-1), where F(n) is that sum for 1..n.
    To compute F(n), group numbers by digit length (1-9, 10-99, 100-999, ...).
    Each group is an arithmetic series, so its sum is (start + end) * count / 2,
    multiplied by the digit length and reduced mod 1e9+7. The final subtraction
    is taken mod 1e9+7 to avoid negatives.

Complexity:
    Time : O(T * log10(R)) since each prefix computation loops once per digit length
    Space: O(1)
"""


# -------------------------------------- Solution -------------------------------------------


MOD = 1000000007

def prefix_sum(n):
    if n <= 0:
        return 0
    ans = 0
    start = 1
    digits = 1
    while start <= n:
        end = min(n, start * 10 - 1)
        count = end - start + 1
        total = (start + end) * count // 2
        ans = (ans + (total % MOD) * digits) % MOD
        start *= 10
        digits += 1
    return ans

def solve():
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        L, R = map(int, input().split())
        answer = (prefix_sum(R) - prefix_sum(L - 1)) % MOD
        print(answer)

if __name__ == "__main__":
    solve()
