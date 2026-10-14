"""
Problem   : Change One (CHANGEONE7)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHANGEONE7
Date      : 2026-10-14
Difficulty: Medium
Topics    : Sorting, Greedy 

Approach  : Sort the array. Changing one element is equivalent to removing it
            from the range calculation, so the only useful candidates are the
            current minimum or maximum. Try dropping each, compute
            (max - min) of what's left, and take the smaller result.

Time      : O(N log N) per test case (sorting dominates)
Space     : O(N) (sorted copy and the slices built when dropping an element)
"""


# -------------------------------------------- Solution -----------------------------------------------------


import sys

def gap_after_drop(arr, skip):
    rest = arr[:skip] + arr[skip + 1:]
    return rest[-1] - rest[0]

def answer_for(arr):
    arr = sorted(arr)
    last = len(arr) - 1
    options = [gap_after_drop(arr, last), gap_after_drop(arr, 0)]
    return min(options)

def run():
    tokens = sys.stdin.read().split()
    pos = 0
    out = []
    cases = int(tokens[pos])
    pos += 1
    for _ in range(cases):
        size = int(tokens[pos])
        pos += 1
        values = list(map(int, tokens[pos:pos + size]))
        pos += size
        out.append(str(answer_for(values)))
    print("\n".join(out))

if __name__ == "__main__":
    run()
