"""
Platform   : CodeChef
Problem    : Equal Reservoir Levels (EQREL)
Link       : https://www.codechef.com/DSAMONDAY022/problems/EQREL
Date       : 2026-09-28
Difficulty : Easy
Topics     : Arrays, Math, Greedy 
Approach   : Every reservoir must end at the lowest level, so the total cost
             is the sum of (level - min). This equals sum(levels) - n * min,
             computed in a single pass that tracks the running sum and min.
Time       : O(n)
Space      : O(n) for the stored input, O(1) extra
"""


# -------------------------------------- Solution ------------------------------------------------


import sys

def _parse(stream):
    tokens = stream.read().split()
    count = int(tokens[0])
    return count, list(map(int, tokens[1:1 + count]))

def _extract_cost(count, levels):
    floor_level = levels[0]
    running_total = 0
    for value in levels:
        running_total += value
        if value < floor_level:
            floor_level = value
    return running_total - floor_level * count

def _entry():
    n, arr = _parse(sys.stdin)
    sys.stdout.write(str(_extract_cost(n, arr)) + "\n")

if __name__ == "__main__":
    _entry()
