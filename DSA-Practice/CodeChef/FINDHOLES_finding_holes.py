"""
Problem   : Finding Holes
Platform  : CodeChef (ICPC Practice — ICPCTR07)
Link      : https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/FINDHOLES
Date      : 2026-09-26
Topics    : Graph Theory, Matrix-Tree Theorem, Linear Algebra, Modular Arithmetic

Approach:
    Build the graph Laplacian matrix L (degree on diagonal, -1 for each edge
    between adjacent vertices). By Kirchhoff's Matrix-Tree Theorem, the number
    of spanning trees of the graph equals the determinant of any (n-1)x(n-1)
    cofactor of L (delete one row and the corresponding column). Compute the
    determinant via Gaussian elimination under modulo 1e9+7, using modular
    inverse (Fermat's little theorem) for pivoting since we're in a finite
    field rather than the reals.

Complexity:
    Time  : O(n^3)  — Gaussian elimination on an (n-1)x(n-1) matrix
    Space : O(n^2)  — storing the Laplacian / reduced matrix
"""


# ----------------------------------------- Solution ----------------------------------------------


import sys
MOD = 1_000_000_007

def build_matrix(n, edges):
    lap = [[0] * n for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        lap[u][u] += 1
        lap[v][v] += 1
        lap[u][v] -= 1
        lap[v][u] -= 1
    return lap

def determinant(mat):
    n = len(mat)
    if n == 0:
        return 1
    result = 1
    for c in range(n):
        p = c
        while p < n and mat[p][c] % MOD == 0:
            p += 1
        if p == n:
            return 0
        if p != c:
            mat[p], mat[c] = mat[c], mat[p]
            result = (-result) % MOD
        x = mat[c][c] % MOD
        result = result * x % MOD
        inv = pow(x, MOD - 2, MOD)
        for r in range(c + 1, n):
            y = mat[r][c] % MOD
            if y == 0:
                continue
            factor = y * inv % MOD
            for j in range(c, n):
                mat[r][j] = (mat[r][j] - factor * mat[c][j]) % MOD
    return result

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    edges = []
    pos = 2
    for _ in range(m):
        u = data[pos]
        v = data[pos + 1]
        edges.append((u, v))
        pos += 2
    if n == 1:
        print(1)
        return
    lap = build_matrix(n, edges)
    reduced = [row[:-1] for row in lap[:-1]]
    print(determinant(reduced))

if __name__ == "__main__":
    solve()
