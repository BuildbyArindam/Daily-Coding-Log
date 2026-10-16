"""
Problem   : Optimal Flip (OPTMFLP18)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/OPTMFLP18
Difficulty: 2006
Date      : 2026-10-16
Topics    : Greedy, Combinatorics, Arrays

Approach:
    Count the subarrays that contain at least one even element, after
    flipping at most one element to maximise that count.
    1. Total subarrays = n(n+1)/2.
    2. A subarray is "bad" if every element in it is odd, so it lies inside
       a maximal run of odd elements. A run of length k contributes k(k+1)/2.
    3. Flipping one element inside a run splits it into two shorter runs.
       The middle element is optimal, giving halves of (k-1)//2 and
       k-1-(k-1)//2. The gain is tri(k) - tri(left) - tri(right).
    4. Only one flip is allowed, so take the largest gain over all runs.
    5. Answer = total - bad + max_gain.
    A sentinel iteration at index pos+n flushes the final run.

Complexity:
    Time : O(n) per test case, single pass.
    Space: O(1) extra per test case (plus the buffered input).
"""


# ------------------------------------------------- Solution -------------------------------------------------------


import sys

def main():
    buf = sys.stdin.buffer.read().split()
    t = int(buf[0])
    pos = 1
    out = []
    tri = lambda k: k * (k + 1) // 2
    for _ in range(t):
        n = int(buf[pos]); pos += 1
        total = tri(n)
        bad = 0       
        gain = 0     
        run = 0
        for idx in range(pos, pos + n + 1):
            odd = idx < pos + n and (int(buf[idx]) & 1)
            if odd:
                run += 1
            elif run:
                left = (run - 1) // 2
                right = run - 1 - left
                before = tri(run)
                bad += before
                red = before - tri(left) - tri(right)
                if red > gain:
                    gain = red
                run = 0
        pos += n
        out.append(total - bad + gain)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
