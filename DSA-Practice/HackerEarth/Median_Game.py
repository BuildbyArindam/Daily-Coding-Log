"""
Problem   : Median Game
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/median-game-june-easy-19-3722be60/
Difficulty: Easy
Topics    : Algorithms, Logic Based, Merge Sort, Sorting
Solved on : 2026-10-25

Approach  : The answer for each test case reduces to max(A) + min(A), so no
            sorting is needed. A single linear pass finds both values.
            Input is read in one shot via sys.stdin.buffer for fast I/O,
            and outputs are joined and written once.

Complexity: Time  - O(N) per test case (O(total N) overall)
            Space - O(N) for the parsed array of a test case
"""


# ------------------------------------------------ Solution -------------------------------------------------------------


import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    tests = int(tokens[0])
    cur = 1
    answers = []
    for _ in range(tests):
        size = int(tokens[cur])
        cur += 1
        nums = list(map(int, tokens[cur:cur + size]))
        cur += size
        answers.append(max(nums) + min(nums))
    sys.stdout.write("\n".join(map(str, answers)) + "\n")

main()
