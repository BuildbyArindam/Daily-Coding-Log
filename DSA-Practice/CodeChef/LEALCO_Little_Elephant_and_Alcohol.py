"""
Problem   : Little Elephant and Alcohol (LEALCO)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/LEALCO
Difficulty: 1810
Date      : 2026-10-11
Topics    : Brute Force, Bitmask, Greedy

Approach:
    If M == 1, any window's max appears at least once, so the answer is -1.
    Otherwise, enumerate every subset of friends (bitmask) who drink one extra
    drink. For each subset, apply the +1 increments and check every window of
    size K: if the max of a window occurs >= M times, the elephant arrests.
    Keep the smallest subset size that leaves no window arrestable.
    Prune any mask whose popcount is already >= the best answer.

Complexity:
    Time : O(T * 2^N * N * K), exponential, only viable for small N
    Space: O(N)

Note: Full constraints need an O(N*K) or O(N^2) greedy over windows.
"""


# ------------------------------------------------ Solution -------------------------------------------------


def solve():
    T = int(input())
    for _ in range(T):
        N, K, M = map(int, input().split())
        R = list(map(int, input().split()))
        if M == 1:
            print(-1)
            continue
        ans = N + 1
        for mask in range(1 << N):
            ops = bin(mask).count('1')
            if ops >= ans:
                continue
            A = R[:]
            for i in range(N):
                if mask & (1 << i):
                    A[i] += 1
            arrested = False
            for i in range(N - K + 1):
                window = A[i:i + K]
                mx = max(window)
                if window.count(mx) >= M:
                    arrested = True
                    break
            if not arrested:
                ans = ops
        print(ans if ans <= N else -1)

if __name__ == "__main__":
    solve()
