"""
Problem: Mark The Answer
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/mark-the-answer-1/
Date: 2026-09-25
Difficulty: Easy
Topics: Data Structures, Arrays, 1-D

Approach:
Greedily count how many problems have difficulty <= max_diff (x).
When a problem exceeds the difficulty cap, use one "skip" allowance
to continue scanning; on a second such problem, stop and return the
count so far. This models a single skip-and-continue rule over an
array scanned in order.

Time complexity: O(n) — single pass over the difficulties list.
Space complexity: O(1) — only a counter and a boolean flag are used.
"""


# --------------------------------------- Solution --------------------------------------------


def compute_score(difficulties, max_diff):
    solved_count = 0
    skip_used = False
    for level in difficulties:
        if level <= max_diff:
            solved_count += 1
        else:
            if not skip_used:
                skip_used = True
                continue
            else:
                break
    return solved_count

def main():
    first_line = input().split()
    n, x = int(first_line[0]), int(first_line[1])
    values = list(map(int, input().split()))
    result = compute_score(values, x)
    print(result)

if __name__ == "__main__":
    main()
