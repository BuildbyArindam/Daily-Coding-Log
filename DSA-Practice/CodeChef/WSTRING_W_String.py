"""
Problem   : W String
Platform  : CodeChef
Link      : https://www.codechef.com/problems/WSTRING
Difficulty: 1809
Topics    : Strings, Prefix Sums 
Date      : 2026-10-10

Approach:
    - Collect the positions of all '#' characters. Fewer than 3 means the answer is 0.
    - Build a 26-letter prefix-count table so the most frequent letter in any
      range can be found in O(26).
    - Slide a window over every 3 consecutive '#' (p1, p2, p3). This splits the
      string into 4 segments (before p1, p1..p2, p2..p3, after p3).
    - In each segment take the highest single-letter frequency. If any segment
      has no letters, the window is invalid.
    - Candidate answer = a + b + c + d + 3 (the three '#'). Keep the maximum.

Complexity:
    Time  : O(26 * n) per test case (prefix build + 4 range queries per window)
    Space : O(26 * n) for the prefix table
"""


# ------------------------------------------------------- Solution ---------------------------------------------------------------------


def solve():
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        s = input().strip()
        n = len(s)
        hashes = [i for i, c in enumerate(s) if c == '#']
        if len(hashes) < 3:
            print(0)
            continue
        pref = [[0] * 26 for _ in range(n + 1)]
        for i, c in enumerate(s):
            pref[i + 1] = pref[i].copy()
            if c != '#':
                pref[i + 1][ord(c) - ord('a')] += 1
        def max_freq(l, r):
            if l > r:
                return 0
            return max(
                pref[r + 1][k] - pref[l][k]
                for k in range(26)
            )
        ans = 0
        for j in range(len(hashes) - 2):
            p1, p2, p3 = hashes[j:j + 3]
            a = max_freq(0, p1 - 1)
            b = max_freq(p1 + 1, p2 - 1)
            c = max_freq(p2 + 1, p3 - 1)
            d = max_freq(p3 + 1, n - 1)
            if a == 0 or b == 0 or c == 0 or d == 0:
                continue
            ans = max(ans, a + b + c + d + 3)
        print(ans)

if __name__ == "__main__":
    solve()
