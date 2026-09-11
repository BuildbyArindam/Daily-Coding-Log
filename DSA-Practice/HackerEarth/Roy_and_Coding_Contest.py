"""
Problem   : Roy and Coding Contest
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roy-and-coding-contest/
Difficulty: Easy
Topics    : Ad-Hoc, Implementation, Math
Date      : 2026-09-11

Approach:
    Simulate the doubling spread of pendrives across computers minute by
    minute: each minute, every computer currently holding a pendrive can
    hand a copy to one computer that doesn't have one, and every free
    pendrive can be assigned to one uncopied computer. This makes both
    `computers` and `pendrives` counts grow roughly geometrically until
    either all N computers have the file or all M pendrives are in use.
    Once pendrives run out (pendrives >= M) but computers < N, the growth
    becomes linear: each of the M pendrives can copy to one new computer
    per minute, so the remaining computers finish in ceil(remaining / M)
    minutes.

Time complexity : O(log(N)) per test case (the doubling loop runs until
                   computers or pendrives saturate, which happens in
                   O(log(N + M)) steps).
Space complexity: O(1) per test case.
"""


# ------------------------- Solution --------------------------------


import sys

def minimum_time(N, M):
    computers = 1
    pendrives = 0
    time = 0
    while computers < N and pendrives < M:
        new_pendrives = min(computers, M - pendrives)
        new_computers = min(pendrives, N - computers)
        computers += new_computers
        pendrives += new_pendrives
        time += 1
    if computers >= N:
        return time
    remaining = N - computers
    time += (remaining + M - 1) // M
    return time

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(minimum_time(N, M))

if __name__ == "__main__":
    main()
