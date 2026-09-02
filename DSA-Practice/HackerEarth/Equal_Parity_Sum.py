"""
Problem: Equal Parity Sum
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/equal-parity-zeros-25eb4114/
Difficulty: Medium
Topics: Greedy Algorithm, Implementation, Linear Search, Algorithms
Date: 2026-09-02

Approach:
Split the array into two "buckets" by position parity: odd-indexed
(1-based) elements sum to S_odd, even-indexed to S_even. If diff =
S_even - S_odd is 0, done. If diff is odd, impossible (flipping a
sign on any element changes the difference by an even number).
Otherwise transform each element to +A[i] (even position) or -A[i]
(odd position), forming array B, and search for a contiguous
subarray of B whose sum equals diff // 2 using a running prefix-sum
hash set (equivalent to flipping the sign of that subarray's
original contribution, which shifts diff by exactly 2*subarray_sum
toward zero).

Time Complexity: O(N) per test case
Space Complexity: O(N) for the prefix sum set
"""


# ------------------------- Solution -------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(data[idx])
        A = [int(x) for x in data[idx+1 : idx+1+N]]
        idx += 1 + N
        S_odd = 0
        S_even = 0
        for i in range(N):
            if (i + 1) % 2 != 0:
                S_odd += A[i]
            else:
                S_even += A[i]
        diff = S_even - S_odd
        if diff == 0:
            out.append("YES")
            continue
        if abs(diff) % 2 != 0:
            out.append("NO")
            continue
        target = diff // 2
        B = [A[i] if (i + 1) % 2 == 0 else -A[i] for i in range(N)]
        prefix_sums = {0}
        current_sum = 0
        found = False
        for val in B:
            current_sum += val
            if (current_sum - target) in prefix_sums:
                found = True
                break
            prefix_sums.add(current_sum)
        if found:
            out.append("YES")
        else:
            out.append("NO")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
