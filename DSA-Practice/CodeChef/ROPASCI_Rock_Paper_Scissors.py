"""
Platform   : CodeChef
Problem    : Rock Paper Scissors (ROPASCI)
Link       : https://www.codechef.com/problems/ROPASCI
Difficulty : 2013
Topics     : Simulation, Suffix Processing, State Compression 
Date       : 2026-10-24

Approach:
    Each of R, P, S is a function on the three moves: when a character c
    is played, every move that c beats becomes c, and the rest stay as they
    are. Instead of simulating the fight for every start position, I keep
    one composed mapping g = (g0, g1, g2) for the suffix of the string.
    I scan right to left. For position j, the answer is g applied to s[j].
    Then I fold K[s[j]] into g, which prepends s[j]'s effect to the suffix
    mapping. Each step is O(1) because the state only has 3 entries.

Complexity:
    Time  : O(N) per test case, O(sum of N) overall
    Space : O(N) for the output buffer (O(1) extra state)
"""


# -------------------------------------------------- Solution ------------------------------------------------------


import sys

def main():
    D = sys.stdin.buffer.read().split()
    Z = {82: 0, 80: 1, 83: 2}      
    L = "RPS"
    K = [[(c if (a + 1) % 3 == c else a) for a in range(3)] for c in range(3)]
    res = []
    q = int(D[0])
    p = 1
    while q:
        q -= 1
        n = int(D[p]); s = D[p + 1]; p += 2
        g0, g1, g2 = 0, 1, 2
        buf = [''] * n
        j = n
        while j:
            j -= 1
            c = Z[s[j]]
            buf[j] = L[(g0, g1, g2)[c]]
            t = K[c]
            g0, g1, g2 = (g0, g1, g2)[t[0]], (g0, g1, g2)[t[1]], (g0, g1, g2)[t[2]]
        res.append(''.join(buf))
    sys.stdout.write('\n'.join(res) + '\n')

main()
