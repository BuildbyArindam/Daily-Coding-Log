"""
Problem   : Count Good Elements (CGOOE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CGOOE
Difficulty: 1259
Topics    : 1D Arrays, Implementation, Data Structures, Arrays, Algorithms
Date      : 2026-10-19

Approach:
    For each index, look at the (up to) 5 elements immediately before it.
    The element is "good" if it is strictly smaller than the minimum of
    that window. The first element has no predecessors, so it is always
    good (handled with a large sentinel). Count the good elements per test.

Complexity:
    Time  : O(N) per test case (window size is capped at 5, so O(5N))
    Space : O(N) for the input array, O(1) extra (window slices are at most 5 elements)
"""


# ---------------------------------------------- Solution --------------------------------------------------------


import sys

def solve_case(values):
    good = 0
    for pos, cur in enumerate(values):
        start = pos - 5 if pos > 5 else 0
        lowest_prev = min(values[start:pos]) if pos else 10 ** 9
        if cur < lowest_prev:
            good += 1
    return good

def main():
    tokens = sys.stdin.read().split()
    cursor = 0
    cases = int(tokens[cursor])
    cursor += 1
    answers = []
    while cases > 0:
        size = int(tokens[cursor])
        cursor += 1
        data = [int(x) for x in tokens[cursor:cursor + size]]
        cursor += size
        answers.append(solve_case(data))
        cases -= 1
    sys.stdout.write("\n".join(map(str, answers)) + "\n")

if __name__ == "__main__":
    main()
