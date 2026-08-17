"""
Problem: Correct Solution?
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/12/B
Date Solved: 2026-08-17
Difficulty: *1100
Topics: Implementation, Sortings

Approach:
Sort the digits of n in ascending order to get the canonical "correct"
answer. If a leading zero appears after sorting (and n isn't just "0"),
swap it with the first non-zero digit to the right — this preserves
sorted order among the remaining digits while eliminating the leading
zero. Compare the constructed string against m to decide OK / WRONG_ANSWER.

Time Complexity:  O(d log d), where d = number of digits in n (dominated by sort)
Space Complexity: O(d), for the digit list/string
"""


# ----------------------- Solution -------------------------------


def solve():
    n = input().strip()
    m = input().strip()
    if n == "0":
        correct = "0"
    else:
        digits = sorted(list(n))
        if digits[0] == "0":
            for i in range(1, len(digits)):
                if digits[i] != "0":
                    digits[0], digits[i] = digits[i], digits[0]
                    break
        correct = "".join(digits)
    if m == correct:
        print("OK")
    else:
        print("WRONG_ANSWER")

if __name__ == "__main__":
    solve()
