"""
Problem   : Final Element (FINELE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FINELE
Difficulty: 1244
Topics    : Bit Manipulation, Math, Lucas' Theorem 
Date      : 2026-10-22

Approach:
    Repeatedly reducing the array by XOR-ing adjacent elements leaves, after n-1
    steps, the XOR of a[i] over every index i where C(n-1, i) is odd. By Lucas'
    theorem, C(n-1, i) is odd exactly when i is a submask of (n-1). So the answer
    is the XOR of a[s] over all submasks s of (n-1), enumerated with
    s = (s - 1) & m.

Complexity:
    Time : O(2^popcount(n-1)) per test, at most O(n), plus O(total input) to read
    Space: O(n) for the buffered input tokens, O(1) extra
"""


# ---------------------------------------------- Solution ----------------------------------------------------


import sys

def main():
    rd = sys.stdin.buffer.read().split()
    t = int(rd[0])
    p = 1
    out = []
    while t:
        t -= 1
        n = int(rd[p])
        p += 1
        base = p
        p += n
        m = n - 1
        res = 0
        s = m
        while True:
            res ^= int(rd[base + s])
            if s == 0:
                break
            s = (s - 1) & m
        out.append(str(res))
    sys.stdout.write("\n".join(out) + "\n")

main()
