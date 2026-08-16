"""
Problem: Old and Cold Numbers
Platform: HackerEarth
Link: http://hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/old-and-cold-numbers-d9326e6b/
Date: 2026-08-16
Difficulty: Easy
Topic: Basic Programming, Implementation

Approach:
    A number is "old" if it's 1 or even; "cold" otherwise.
    For each query range [l, r], majority must be old (>= ceil(len/2)).
    Precompute prefix sums of old-count so each query range's old count
    is O(1) via prefix_old[r] - prefix_old[l-1].
    Answer = max(0, required_old - actual_old_count), i.e. minimum
    conversions needed to make old numbers the majority in that range.

Time Complexity:  O(n + q) per test case (O(n) prefix build + O(1) per query)
Space Complexity: O(n) for the prefix sum array
"""


# ----------------------- Solution ---------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    num_test_cases = int(next(iterator))
    out = []
    for _ in range(num_test_cases):
        n = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]
        prefix_old = [0] * (n + 1)
        for i in range(n):
            is_old = 1 if (a[i] == 1 or a[i] % 2 == 0) else 0
            prefix_old[i + 1] = prefix_old[i] + is_old
        q = int(next(iterator))
        for _ in range(q):
            l = int(next(iterator))
            r = int(next(iterator))
            length = r - l + 1
            old_count = prefix_old[r] - prefix_old[l - 1]
            required_old = (length + 1) // 2
            needed_steps = max(0, required_old - old_count)
            out.append(str(needed_steps))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
