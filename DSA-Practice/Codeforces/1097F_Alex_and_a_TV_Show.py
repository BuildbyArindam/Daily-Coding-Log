"""
Problem   : Alex and a TV Show
Platform  : Codeforces
Link      : https://codeforces.com/contest/1097/problem/F
Rating    : *2500
Tags      : bitmasks, combinatorics, number theory (Mobius inversion)
Solved on : 2026-08-15

Approach
--------
Each array slot b[i] is not a number but a "multiset signature" encoded as a
big bitmask: bit d is set in b[i] iff an odd number of elements currently
represented by b[i] are divisible by d (build_divmask constructs this for a
single value on a type-1 assignment). Type-2/3 ops (XOR/AND) combine these
signatures directly as bitmask XOR/AND, since XOR of divisor-bitmasks = the
divisor-bitmask of the symmetric-difference multiset (parity of counts).

To answer "does value y occur an odd number of times" (type-4), use Mobius
inversion:
    parity(count of y) = XOR over squarefree s of [ bit (y*s) set in b[x] ]
                        = popcount( b[x] & bas[y] ) mod 2
where bas[y] has a bit set at position y*s for every squarefree s with
y*s <= MAXV. Only squarefree s contribute because mu(s) = 0 kills the rest,
and since we only care about parity, the +-1 sign of mu(s) doesn't matter -
only whether s is squarefree does.

Precompute:
  - mu[] via linear sieve -> squarefree list
  - divmask[v]: bitmask of divisors of v          (O(V log V) sieve-style build)
  - bas[y]: bitmask of {y*s : s squarefree, y*s<=V} (O(V log V), harmonic sum)

Complexity
----------
Preprocessing : O(V log V) time, O(V) sieve arrays
                + O(V^2 / w) bits for divmask/bas tables (w = machine word,
                  here effectively Python bigint limb width)
Per query     : O(V / w) amortized for XOR/AND/popcount on V-bit Python ints
                (Python big-int ops are word-parallel under the hood)
Space         : O(V) big integers of up to V bits each  ~ O(V^2 / w) words,
                V = 7000 here, comfortably within CF's memory limit
"""

# ---------------------------------Solutionn-------------------------------------


import sys
MAXV = 7000

def build_mobius_and_squarefree():
    """Linear sieve for the Möbius function."""
    mu = [0] * (MAXV + 1)
    composite = bytearray(MAXV + 1)
    primes = []
    mu[1] = 1
    for i in range(2, MAXV + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            x = i * p
            if x > MAXV:
                break
            composite[x] = 1
            if i % p == 0:
                mu[x] = 0
                break
            else:
                mu[x] = -mu[i]
    squarefree = [i for i in range(1, MAXV + 1) if mu[i] != 0]
    return squarefree

def build_divmask():
    """
    divmask[v] has bit d set iff d divides v.

    This is the Python equivalent of the bitset created for
    a type-1 operation.
    """
    divmask = [0] * (MAXV + 1)
    for d in range(1, MAXV + 1):
        bit = 1 << d
        for v in range(d, MAXV + 1, d):
            divmask[v] |= bit
    return divmask

def build_bas(squarefree):
    """
    bas[y] has bit (y * s) set for every squarefree s such that
    y * s <= MAXV.

    This exactly matches:

        for i = 1..7000
            for squarefree a
                bas[i][i*a] = 1
    """
    bas = [0] * (MAXV + 1)
    for s in squarefree:
        bit_shift_factor = s
        for y in range(1, MAXV // s + 1):
            bas[y] |= 1 << (y * bit_shift_factor)
    return bas

def main():
    input = sys.stdin.buffer.readline
    n, q = map(int, input().split())
    squarefree = build_mobius_and_squarefree()
    divmask = build_divmask()
    bas = build_bas(squarefree)
    b = [0] * (n + 1)
    output = []
    for _ in range(q):
        data = list(map(int, input().split()))
        op = data[0]
        x = data[1]
        y = data[2]
        if op == 1:
            b[x] = divmask[y]
        elif op == 2:
            z = data[3]
            b[x] = b[y] ^ b[z]
        elif op == 3:
            z = data[3]
            b[x] = b[y] & b[z]
        else:
            output.append(
                '1' if ((b[x] & bas[y]).bit_count() & 1) else '0'
            )
    sys.stdout.write(''.join(output))

if __name__ == "__main__":
    main()
