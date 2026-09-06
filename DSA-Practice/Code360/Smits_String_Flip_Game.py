"""
Problem   : Smit's String Flip Game
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/smit-s-string-flip-game_5714668
Difficulty: Hard
Date      : 2026-09-06

Approach:
    Simulate the transformation, where new_str[i] = '1' if str[i-1] == str[i+1]
    else '0' (endpoints stay '0'). Since the string is over a finite alphabet
    and has fixed length n, repeated transformation must eventually enter a
    cycle. Track each seen state in a dict {state: step_index}. Once a repeat
    is detected, compute cycle_length and fast-forward the remaining steps
    using (remaining % cycle_length) instead of simulating one-by-one, which
    avoids TLE for very large k.

Time Complexity : O(n^2) worst case
    - Each simulation step rebuilds the string in O(n).
    - At most O(n) distinct states can occur before a cycle repeats
      (bounded by the state-transition structure), so up to O(n) steps
      before either finishing or detecting the cycle.
Space Complexity: O(n^2) worst case
    - The `seen` dict can store up to O(n) strings, each of length n.
"""


# ---------------------------- Solution ---------------------------------


from os import *
from sys import *
from collections import *
from math import *
from builtins import open

def finalString(n: int, k: int, str: str) -> str:
    if k == 0:
        return str
    seen = {}
    step = 0
    while step < k:
        if str in seen:
            cycle_start = seen[str]
            cycle_length = step - cycle_start
            remaining = k - step
            if cycle_length > 0:
                skip = remaining // cycle_length
                if skip > 0:
                    step += skip * cycle_length
                    continue
        else:
            seen[str] = step
        new_str = ['0'] * n
        for i in range(1, n - 1):
            if str[i - 1] == str[i + 1]:
                new_str[i] = '1'
        str = ''.join(new_str)
        step += 1
    return str
