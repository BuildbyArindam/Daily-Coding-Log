"""
Problem   : Additive Dissonance
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ADDIS
Date      : 2026-09-10
Difficulty: Easy–Medium
Topics    : Frequency Counting, Greedy, Math

Approach  :
    For each test case, count the frequency of every element in A.
    Let f = the highest frequency among all elements.
    The answer is ceil(f / 2) — the most-repeated value is the
    bottleneck; pairing up its duplicate occurrences and resolving
    them two at a time gives the minimum number of operations needed.

Time Complexity  : O(N) per test case  ->  O(sum(N)) overall
Space Complexity : O(N) per test case, for the frequency Counter
"""





import sys
from collections import Counter

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        max_freq = max(Counter(A).values())
        print((max_freq + 1) // 2)

if __name__ == "__main__":
    solve()
