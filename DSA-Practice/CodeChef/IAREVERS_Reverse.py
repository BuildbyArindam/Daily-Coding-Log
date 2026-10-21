"""
Problem   : Reverse (IAREVERS)
Platform  : CodeChef (ZCO / INOI practice)
Link      : https://www.codechef.com/practice/course/zco-inoi-problems/IARCSJUD/problems/IAREVERS
Date      : 2026-10-21
Difficulty: Medium
Topics    : Strings, Implementation

Approach:
    Read N lines and process them from last to first. For each line, strip
    the punctuation characters (' . , ; :), split into words, reverse the
    word order and join with single spaces. Output the results in that order.

Complexity:
    Time  : O(L), where L is the total number of characters in the input
            (each character is cleaned, split and joined a constant number of times)
    Space : O(L) for the stored lines and the output buffer
"""


# ---------------------------------------- Solution ----------------------------------------------------


import sys

def clean(s):
    junk = {"'", ".", ",", ";", ":"}
    return "".join(ch for ch in s if ch not in junk)

def flip_words(s):
    parts = clean(s).split()
    parts.reverse()
    return " ".join(parts)

def run():
    raw = sys.stdin.read().split("\n")
    total = int(raw[0].strip())
    body = raw[1:1 + total]
    while len(body) < total:
        body.append("")
    out = []
    idx = total - 1
    while idx >= 0:
        out.append(flip_words(body[idx]))
        idx -= 1
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    run()
