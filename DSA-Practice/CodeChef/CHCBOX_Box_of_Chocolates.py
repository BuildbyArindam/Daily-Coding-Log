"""
Platform   : CodeChef
Problem    : Box of Chocolates (CHCBOX)
Link       : https://www.codechef.com/problems/CHCBOX
Difficulty : 1730
Topics     : Sliding Window, Circular Array
Date       : 2026-10-08

Approach:
    Treat the array as circular and slide a window of size N//2 across all
    N starting positions. Keep a running count of how many maximum-weight
    elements are inside the window. When the window moves one step, drop the
    outgoing element and add the incoming one (index taken modulo N), each
    updating the count in O(1). Count the windows where that count is 0.

Complexity:
    Time  : O(N) per test case
    Space : O(1) extra (besides the input array)
"""



# ------------------------------------- Solution ----------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        W = list(map(int, input().split()))
        half = N // 2
        mx = max(W)
        max_count = 0
        ans = 0
        for i in range(half):
            if W[i] == mx:
                max_count += 1
        if max_count == 0:
            ans += 1
        for start in range(1, N):
            if W[start - 1] == mx:
                max_count -= 1
            entering = (start + half - 1) % N
            if W[entering] == mx:
                max_count += 1
            if max_count == 0:
                ans += 1
        print(ans)

if __name__ == "__main__":
    solve()
