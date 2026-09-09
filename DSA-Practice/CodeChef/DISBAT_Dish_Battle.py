"""
Problem   : Dish Battle (DISBAT)
Link      : https://www.codechef.com/problems/DISBAT
Date      : 2026-09-09
Difficulty: Easy
Topics    : Disjoint Set Union (Union-Find), Union by Value, Path Compression

Approach:
    Each chef starts as their own DSU component, with max_score tracking
    the highest-scoring dish owned by that component's root.
    - Query type 1 x: find(x) returns the current root (winning chef) of x.
    - Query type 2 x y: find roots of x and y. If same root -> "Invalid query!".
      Otherwise the component with the higher max_score absorbs the other
      (loser's root is re-parented to winner's root); scores are equal -> no-op.

Complexity:
    Time  : O((N + Q) log N) amortized per test case (path compression only,
            no union-by-rank, so worst-case chains are possible but rare in practice)
    Space : O(N)
"""


# ---------------------------- Solution -----------------------------------


import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.max_score = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_winner(self, winner, loser):
        self.parent[loser] = winner
        if self.max_score[loser] > self.max_score[winner]:
            self.max_score[winner] = self.max_score[loser]

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    sys.setrecursionlimit(10**6)
    for _ in range(t):
        n = int(input())
        dsu = DSU(n)
        s = [0] + list(map(int, input().split()))
        for i in range(1, n + 1):
            dsu.max_score[i] = s[i]
        q = int(input())
        for _ in range(q):
            query = list(map(int, input().split()))
            if query[0] == 1:
                x = query[1]
                print(dsu.find(x))
            else:
                x, y = query[1], query[2]
                chef_x = dsu.find(x)
                chef_y = dsu.find(y)
                if chef_x == chef_y:
                    print("Invalid query!")
                    continue
                score_x = dsu.max_score[chef_x]
                score_y = dsu.max_score[chef_y]
                if score_x == score_y:
                    continue
                if score_x > score_y:
                    dsu.union_winner(chef_x, chef_y)
                else:
                    dsu.union_winner(chef_y, chef_x)
