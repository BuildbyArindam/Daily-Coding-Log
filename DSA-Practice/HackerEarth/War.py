"""
Problem   : War
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/warcakewalk/
Difficulty: Easy
Topics    : Approved, Basic Programming, Open
Date      : 2026-08-27

Approach:
For each test case, read Bob's and Alice's arrays and compare their
maximum values. Whoever has the higher max wins; equal maxes -> Tie.
Fast I/O via sys.stdin read-all + index-based parsing to handle large inputs.

Time complexity : O(N) per test case (single pass to find each max) -> O(sum(N)) overall
Space complexity: O(N) per test case for the sliced arrays (O(1) extra beyond input storage)
"""


# -------------------------- Solution -------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        bob_max = max(map(int, input_data[idx:idx + n]))
        idx += n
        alice_max = max(map(int, input_data[idx:idx + n]))
        idx += n
        if bob_max > alice_max:
            out.append("Bob")
        elif alice_max > bob_max:
            out.append("Alice")
        else:
            out.append("Tie")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
