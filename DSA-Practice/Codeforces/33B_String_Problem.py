"""
Problem: String Problem
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/33/B
Difficulty: *1800
Date Solved: 2026-09-01
Topic: Shortest Path (Floyd-Warshall on character graph)

Approach:
Model each lowercase letter (26 total) as a node in a directed graph, where an
edge a->b with weight w means "character a can be changed into character b at
cost w" (a character can also stay unchanged at cost 0). Run Floyd-Warshall
over this 26-node graph to get the minimum conversion cost between every pair
of letters. Then, for each position i where s[i] != t[i], find the cheapest
common target character c such that s[i] can become c and t[i] can become c,
minimizing dist[s[i]][c] + dist[t[i]][c] over all c. Sum these costs; if any
position has no reachable common character, output -1.

Time Complexity:  O(26^3 + n*26) — Floyd-Warshall dominates
Space Complexity: O(26^2) for the distance matrix
"""


# ------------------------- Solution ----------------------------------


import sys

def solve():
    input = sys.stdin.readline
    s = input().strip()
    t = input().strip()
    n = int(input())
    INF = 10**18
    dist = [[INF] * 26 for _ in range(26)]
    for i in range(26):
        dist[i][i] = 0
    for _ in range(n):
        a, b, w = input().split()
        a = ord(a) - ord('a')
        b = ord(b) - ord('a')
        w = int(w)
        dist[a][b] = min(dist[a][b], w)
    for k in range(26):
        for i in range(26):
            if dist[i][k] == INF:
                continue
            for j in range(26):
                if dist[k][j] == INF:
                    continue
                new_dist = dist[i][k] + dist[k][j]
                if new_dist < dist[i][j]:
                    dist[i][j] = new_dist
    if len(s) != len(t):
        print(-1)
        return
    answer = []
    total_cost = 0
    for a, b in zip(s, t):
        x = ord(a) - ord('a')
        y = ord(b) - ord('a')
        if x == y:
            answer.append(a)
            continue
        best_cost = INF
        best_char = -1
        for c in range(26):
            if dist[x][c] == INF or dist[y][c] == INF:
                continue
            cost = dist[x][c] + dist[y][c]
            if cost < best_cost:
                best_cost = cost
                best_char = c
        if best_char == -1:
            print(-1)
            return
        total_cost += best_cost
        answer.append(chr(best_char + ord('a')))
    print(total_cost)
    print(''.join(answer))

if __name__ == "__main__":
    solve()
