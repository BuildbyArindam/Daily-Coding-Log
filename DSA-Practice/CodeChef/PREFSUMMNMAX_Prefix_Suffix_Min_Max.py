"""
Platform   : CodeChef
Problem    : Prefix Suffix Min Max
Link       : https://www.codechef.com/problems/PREFSUMMNMAX
Difficulty : 2014
TOpics     : Constructive, Algorithms
Date       : 2026-10-24

Approach:
    For each test case, the answer starts with a fixed value of 2 * 10^6,
    followed by the difference between each pair of adjacent elements
    (A[i] - A[i-1]). The input is read in one pass with a single
    buffered read for speed.

Time Complexity  : O(N) per test case, O(sum of N) overall
Space Complexity : O(N) per test case for the parsed array and output
"""


# ---------------------------------------------- Solution ---------------------------------------------------


import sys as _s
from itertools import chain as _c

def _solve(_blk):
    _top = 2 * 10 ** 6
    _prev = _blk[0]
    _out = [_top]
    _push = _out.append
    for _v in _blk[1:]:
        _push(_v - _prev)
        _prev = _v
    return " ".join(map(str, _out))

def _main():
    _raw = _s.stdin.buffer.read().split()
    _t = int(_raw[0])
    _pos = 1
    _res = []
    for _ in range(_t):
        _n = int(_raw[_pos])
        _pos += 1
        _chunk = list(map(int, _raw[_pos:_pos + _n]))
        _pos += _n
        _res.append(_solve(_chunk))
    _s.stdout.write("\n".join(_res) + "\n")

if __name__ == "__main__":
    _main()
