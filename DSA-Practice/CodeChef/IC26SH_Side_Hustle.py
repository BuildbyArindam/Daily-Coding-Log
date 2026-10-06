"""
Problem   : Side Hustle (IC26SH)
Platform  : CodeChef (ICPCOL26POST)
Link      : https://www.codechef.com/ICPCOL26POST/problems/IC26SH
Date      : 2026-10-06
Difficulty: Medium 
Topics    : Permutations, Cycle Decomposition, Greedy, Sorting

Approach
--------
1. Decompose the permutation into disjoint cycles with a visited array.
   Cycles are independent, so the answer is the sum of each cycle's best value.
2. Cycle of length 1: take its gain directly.
3. Cycle of length L > 1: compare two strategies and keep the better one.
   a) Take every element: sum(gain) - (L - 1) * cost.
   b) Take a partial set: sort gains in descending order and greedily add
      (gain - cost) while it is positive, using at most L - 2 elements.
4. Add the best value of each cycle to the total.

Complexity
----------
Time  : O(N log N) per test case (sorting inside each cycle; total cycle
        length is N).
Space : O(N) for the visited array and the per-cycle value list.
"""


# ---------------------------------------- Solution --------------------------------------------------------


import sys

def main():
    buf = sys.stdin.buffer.read().split()
    ptr = 0
    T = int(buf[ptr]); ptr += 1
    out = []
    while T:
        T -= 1
        n = int(buf[ptr]); cst = int(buf[ptr + 1]); ptr += 2
        perm = [int(x) - 1 for x in buf[ptr:ptr + n]]; ptr += n
        gain = buf[ptr:ptr + n]; ptr += n
        gain = [int(x) for x in gain]
        seen = bytearray(n)
        answer = 0
        for s in range(n):
            if seen[s]:
                continue
            vals = []
            j = s
            while not seen[j]:
                seen[j] = 1
                vals.append(gain[j])
                j = perm[j]
            ln = len(vals)
            if ln == 1:
                answer += vals[0]
                continue
            full = sum(vals) - (ln - 1) * cst
            vals.sort(reverse=True)
            part = 0
            lim = ln - 2
            for q in range(lim):
                d = vals[q] - cst
                if d <= 0:
                    break
                part += d
            answer += part if part > full else full
        out.append(answer)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
