"""
Platform  : CodeChef (START258B)
Problem   : MEX Game (Medium)
Link      : https://www.codechef.com/START258B/problems/MEXGAME1
Date      : 2026-09-30
Topics    : Game Theory, Parity, MEX, Math

Approach:
    The winner is decided by the parity of the total number of moves.
    1. Count frequencies and compute the MEX of the array.
    2. The game stops at a terminal state: values 0..MEX-1 each stay once
       (sum = MEX*(MEX-1)/2), and every element greater than MEX is reduced
       to MEX+1 (contributing (MEX+1) * count).
    3. Total moves = initial sum - terminal sum.
       Odd -> Alice wins, even -> Bob wins.

Complexity:
    Time  : O(N) per test case (single pass for counts, MEX scan capped at 102)
    Space : O(1) extra (fixed-size frequency array of 102), O(N) for input
"""


# --------------------------------- Solution ---------------------------------------------


import sys

def _read_tokens():
    return sys.stdin.buffer.read().split()

def _mex_of(counts, cap):
    val = 0
    while val < cap and counts[val] > 0:
        val += 1
    return val

def _terminal_energy(mex_val, big_cnt):
    below = mex_val * (mex_val - 1) // 2
    frozen = (mex_val + 1) * big_cnt
    return below + frozen

def _judge_case(nums):
    LIMIT = 102
    freq = [0] * LIMIT
    running_sum = 0
    for x in nums:
        freq[x] += 1
        running_sum += x
    mex_val = _mex_of(freq, LIMIT)
    above_cnt = 0
    for x in nums:
        if x > mex_val:
            above_cnt += 1
    rest_energy = _terminal_energy(mex_val, above_cnt)
    remaining_moves = running_sum - rest_energy
    return "Alice" if remaining_moves & 1 else "Bob"

def main():
    tokens = _read_tokens()
    pos = 0
    t_cases = int(tokens[pos]); pos += 1
    results = []
    for _ in range(t_cases):
        n = int(tokens[pos]); pos += 1
        row = tokens[pos:pos + n]
        pos += n
        arr = [int(v) for v in row]
        results.append(_judge_case(arr))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
