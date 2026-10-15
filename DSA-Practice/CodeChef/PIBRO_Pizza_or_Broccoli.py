"""
Problem   : Pizza or Broccoli (PIBRO)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/PIBRO
Difficulty: 2000
Date      : 2026-10-15
Topics    : String, Sliding Window, Two Pointers, Greedy

Approach:
    Precompute tail[i], the run of consecutive '1's ending just before index i,
    and head[i], the run of consecutive '1's starting at index i. Slide a window
    of length k over the string. Placing the k-block at [st, st+k) joins the
    '1'-run on its left with the '1'-run on its right, giving
    tail[st] + k + head[st+k]. The answer is the maximum over all windows.

Time Complexity : O(n) per test case
Space Complexity: O(n) for the tail/head arrays
"""


# -------------------------------------------- Solution --------------------------------------------------


import sys

def best_for_case(k, s):
    n = len(s)
    tail = [0] * (n + 1)
    for i in range(n):
        tail[i + 1] = tail[i] + 1 if s[i] == '1' else 0
    head = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        head[i] = head[i + 1] + 1 if s[i] == '1' else 0
    top = 0
    for st in range(n - k + 1):
        cand = tail[st] + k + head[st + k]
        if cand > top:
            top = cand
    return top

def main():
    tokens = sys.stdin.read().split()
    t = int(tokens[0])
    pos = 1
    answers = []
    for _ in range(t):
        n = int(tokens[pos])
        k = int(tokens[pos + 1])
        s = tokens[pos + 2]
        pos += 3
        answers.append(str(best_for_case(k, s)))
    sys.stdout.write("\n".join(answers) + "\n")

if __name__ == "__main__":
    main()
