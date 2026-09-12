"""
Problem: Tower of Hanoi
Platform: Code360 (Coding Ninjas / Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380918
Date: 2026-09-12
Difficulty: Easy
Topics: Recursion, Divide and Conquer

Approach:
Classic recursive Tower of Hanoi. To move n disks from source to destination
using auxiliary as the helper peg:
  1. Move top (n-1) disks from source -> auxiliary (using destination as helper)
  2. Move the nth (largest) disk from source -> destination
  3. Move (n-1) disks from auxiliary -> destination (using source as helper)
Base case: n == 0 means no disks left to move, so return.

Time Complexity: O(2^n) — each call spawns two recursive calls, and there are
                  exactly 2^n - 1 moves for n disks.
Space Complexity: O(n) — recursion stack depth (excluding the output list,
                  which itself grows to O(2^n) entries).
"""


# ------------------------------ Solution ----------------------------------


def towerOfHanoi(n):
    ans = []
    def solve(n, source, destination, auxiliary):
        if n == 0:
            return
        solve(n - 1, source, auxiliary, destination)
        ans.append([source, destination])
        solve(n - 1, auxiliary, destination, source)
    solve(n, 1, 3, 2)
    return ans
