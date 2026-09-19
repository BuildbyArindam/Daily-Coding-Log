"""
Problem: The Robotics Assembly Kit
Platform: Unstop
Link: https://unstop.com/code/practice/660830
Date Solved: 2026-09-19
Difficulty: Medium
Topics: String, Array, Sliding Window, Two Pointers, Hashing, Frequency Counting

Approach:
Read the string and a set of (char, required_count) constraints. First verify
feasibility by checking overall character frequencies against requirements
(if any required char is short in supply, answer is -1). Then use a
variable-size sliding window (two pointers) to find the smallest substring
that satisfies all frequency requirements simultaneously — expand `right`,
update per-window counts, track how many requirement "types" are currently
satisfied, and once all are satisfied, shrink `left` to minimize the window
while re-checking satisfaction after each removal.

Time Complexity: O(n + m), where n = len(s), m = number of required chars
  (each pointer traverses s at most once; frequency dict ops are O(1))
Space Complexity: O(n + m) for the total/need/have frequency dictionaries
"""


# --------------------------------------- Solution ------------------------------------------


import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    s = input().strip()
    tokens = []
    while len(tokens) < 2 * m:
        tokens.extend(input().split())
    need = {}
    for i in range(0, 2 * m, 2):
        ch = tokens[i]
        cnt = int(tokens[i + 1])
        need[ch] = cnt
    total = {}
    for ch in s:
        total[ch] = total.get(ch, 0) + 1
    for ch, cnt in need.items():
        if total.get(ch, 0) < cnt:
            print(-1)
            return
    have = {}
    satisfied = 0
    required_types = len(need)
    left = 0
    ans = n + 1
    for right, ch in enumerate(s):
        if ch in need:
            have[ch] = have.get(ch, 0) + 1
            if have[ch] == need[ch]:
                satisfied += 1
        while satisfied == required_types:
            ans = min(ans, right - left + 1)
            left_ch = s[left]
            if left_ch in need:
                have[left_ch] -= 1
                if have[left_ch] < need[left_ch]:
                    satisfied -= 1
            left += 1
    print(ans if ans <= n else -1)

if __name__ == "__main__":
    main()
