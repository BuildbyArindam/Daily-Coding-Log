"""
Problem   : Water Moving (Min)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/WATERMOVE
Date      : 2026-10-14
Difficulty: Medium
Topics    : Greedy, Sorting 

Approach  : Greedy + sorting. After sorting, the best merge combines the two
            smallest values. The answer is the larger of that merged sum and
            the current maximum, so the maximum never drops below the largest
            original value.

Complexity: Time  - O(N log N) per test case (dominated by the sort)
            Space - O(N) for the input row
"""


# ----------------------------------------------- Solution -----------------------------------------------------------


import sys

def solve_case(vals):
    vals.sort()
    merged = vals[0] + vals[1]
    biggest = vals[-1]
    return merged if merged > biggest else biggest

def main():
    tokens = sys.stdin.read().split()
    ptr = 0
    cases = int(tokens[ptr])
    ptr += 1
    answers = []
    for _ in range(cases):
        n = int(tokens[ptr])
        k = int(tokens[ptr + 1]) 
        ptr += 2
        row = [int(x) for x in tokens[ptr:ptr + n]]
        ptr += n
        answers.append(str(solve_case(row)))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
