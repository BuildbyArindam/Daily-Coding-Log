"""
Problem   : Special String
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/special-string_893270?kunjiRedirection=true
Date      : 2026-08-28
Difficulty: Medium
Topics    : Greedy, Backtracking / Constructive Algorithms, String Manipulation

Approach:
Find the lexicographically smallest string >= s of length n over the first
p lowercase letters such that no character repeats within the previous
2 positions (arr[i] != arr[i-1] and arr[i] != arr[i-2]).

Scan from the rightmost index backwards. At each position i, try to bump
its character to something strictly greater than the original (respecting
the no-repeat-in-last-2 rule). If a valid bump is found, greedily fill
every position after i with the smallest valid character. If the fill
succeeds for the whole suffix, that's the answer; otherwise backtrack i
one step further left. If no position can be bumped, no valid string >= s
exists -> return "NO".

Time complexity : O(n^2 * p) worst case
                   (outer loop over n positions x up to p candidate chars
                   x O(n*p) suffix-fill attempt)
Space complexity: O(n) for the working character array
"""


# ---------------------------- Solution ----------------------------------


from os import *
from sys import *
from collections import *
from math import *

def specialString(s, n, p):
    def valid_char(ch, pos, arr):
        if pos >= 1 and arr[pos - 1] == ch:
            return False
        if pos >= 2 and arr[pos - 2] == ch:
            return False
        return True
    arr = list(s)
    for i in range(n - 1, -1, -1):
        current = ord(arr[i]) - ord('a')
        for c in range(current + 1, p):
            ch = chr(ord('a') + c)
            if not valid_char(ch, i, arr):
                continue
            arr[i] = ch
            possible = True
            for j in range(i + 1, n):
                placed = False
                for x in range(p):
                    nxt = chr(ord('a') + x)
                    if valid_char(nxt, j, arr):
                        arr[j] = nxt
                        placed = True
                        break
                if not placed:
                    possible = False
                    break
            if possible:
                return ''.join(arr)
            arr[i] = s[i]
    return "NO"

if __name__ == "__main__":
    input = stdin.readline
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        s = input().strip()
        print(specialString(s, n, p))
