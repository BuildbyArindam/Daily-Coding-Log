"""
Problem: Tag Validator
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/tag-validator_1279650?kunjiRedirection=true
Difficulty: Medium
Date Solved: 2026-08-24
Topics: Stack, String Parsing/Simulation

Approach:
Single left-to-right scan using a stack to track open tag names.
- On '<' : detect CDATA sections (skip verbatim to "]]>"), closing tags
  ("</NAME>", must match stack top), or opening tags ("<NAME>", pushed
  onto stack). Tag/content is only valid outside CDATA if the stack is
  non-empty (i.e., inside some tag).
- Reject if a tag name isn't 1-9 uppercase letters, malformed closing
  tags, or content/tags appearing outside the outermost tag.
- Valid iff the stack is empty at the end (all tags closed) and the
  string starts with '<'.

Time Complexity: O(n) — single pass, each index processed once
Space Complexity: O(n) — stack holds nested tag names in the worst case
"""


# -------------------------- Solution -----------------------------


from os import *
from sys import *
from collections import *
from math import *

def tagParser(s):
    # Write your code here 
    n = len(s)
    stack = []
    i = 0
    if n == 0 or s[0] != '<':
        return False
    while i < n:
        if s[i] != '<':
            if not stack:
                return False
            i += 1
            continue
        if s.startswith("<![CDATA[", i):
            if not stack:
                return False
            end = s.find("]]>", i + 9)
            if end == -1:
                return False
            i = end + 3
            continue
        if s.startswith("</", i):
            j = i + 2
            while j < n and 'A' <= s[j] <= 'Z':
                j += 1
            name = s[i + 2:j]
            if not (1 <= len(name) <= 9):
                return False
            if j >= n or s[j] != '>':
                return False
            if not stack or stack[-1] != name:
                return False
            stack.pop()
            i = j + 1
            if not stack and i != n:
                return False
            continue
        j = i + 1
        while j < n and 'A' <= s[j] <= 'Z':
            j += 1
        name = s[i + 1:j]
        if not (1 <= len(name) <= 9):
            return False
        if j >= n or s[j] != '>':
            return False
        if not stack and i != 0:
            return False
        stack.append(name)
        i = j + 1
    return len(stack) == 0

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print("True" if tagParser(s) else "False")
