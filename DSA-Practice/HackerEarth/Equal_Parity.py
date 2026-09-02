"""
Problem: Equal Parity
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/equal-parity-ccc0c1dd/
Difficulty: Easy
Topics: Linear Search, Algorithms, Greedy Algorithm
Date Solved: 2026-09-02

Approach:
For each element, count how many times it's divisible by 2 (i.e., its
power-of-2 factor / count of trailing "halvings"). Sum these counts across
the array. If the total number of halving operations available is >= N,
we can always make all N elements share the same parity (by repeatedly
halving odd-parity-causing elements down as needed); otherwise it's
impossible.

Time Complexity: O(N log(max(A))) per test case — each element is halved
                  at most log2(A[i]) times.
Space Complexity: O(N) — for storing the input array.
"""


# -------------------------- Solution -------------------------------------


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    total_twos = 0
    for x in A:
        while x % 2 == 0:
            total_twos += 1
            x //= 2
    if total_twos >= N:
        print("YES")
    else:
        print("NO")
