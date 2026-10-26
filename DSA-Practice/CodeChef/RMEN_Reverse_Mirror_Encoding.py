"""
Problem   : Reverse Mirror Encoding (RMEN)
Platform  : CodeChef (DSAMONDAY026)
Link      : https://www.codechef.com/DSAMONDAY026/problems/RMEN
Date      : 2026-10-26
Difficulty: Hard
Topics    : Strings, Implementation

Approach  : Single left-to-right pass over the string. For each character,
            peek at the next one: if it is '#', the character is "marked"
            and is mirrored as chr(233 - code), consuming both characters.
            Otherwise it is mirrored as chr(207 - code), consuming one.
            Results are collected in a list and joined once at the end.

Time      : O(n), each character is visited once
Space     : O(n) for the output buffer
"""


# --------------------------------------------- Solution ----------------------------------------------------------


import sys

def main():
    raw = sys.stdin.readline().strip()
    n = len(raw)
    out = []
    pos = 0
    while pos < n:
        code = ord(raw[pos])
        marked = pos + 1 < n and raw[pos + 1] == '#'
        if marked:
            out.append(chr(233 - code))
            pos += 2
        else:
            out.append(chr(207 - code))
            pos += 1
    print("".join(out))

main()
