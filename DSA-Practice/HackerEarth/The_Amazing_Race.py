"""
Problem: The Amazing Race
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/the-amazing-race-1/
Date: 2026-09-12
Difficulty: Medium
Topic: Data Structures, Implementation

Approach:
    For each position i, find the number of visible flags to its left and
    right — a flag is visible if there's no taller flag between it and i.
    Use two monotonic (decreasing) stacks to compute, for every index,
    the distance to the nearest strictly taller flag on each side in O(n).
    Total visibility count at i = left[i] + right[i]; multiply by (i+1)
    to weight by position, and track the max (mod 1e9+7).

Time Complexity:  O(n) per test case (two single passes with a monotonic stack)
Space Complexity: O(n) (stack + left/right arrays)
"""


# ------------------------- Solution ------------------------------


import sys
MOD = 1000000007
input = sys.stdin.buffer.readline

def solve():
    t = int(input())
    output = []
    for _ in range(t):
        n = int(input())
        h = list(map(int, input().split()))
        left = [0] * n
        stack = []
        for i in range(n):
            while stack and h[stack[-1]] < h[i]:
                stack.pop()
            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i
            stack.append(i)
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and h[stack[-1]] < h[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = n - 1 - i
            stack.append(i)
        best_sight = -1
        answer = 0
        for i in range(n):
            x = left[i] + right[i]
            sight = (x * (i + 1)) % MOD
            if sight > best_sight:
                best_sight = sight
                answer = i + 1
        output.append(str(answer))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
