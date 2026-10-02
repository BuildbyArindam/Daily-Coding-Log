"""
Platform   : CodeChef
Problem    : Little Elephant and Order (LUCKY10)
Link       : https://www.codechef.com/problems/LUCKY10
Difficulty : 1722
Topics     : Greedy, Counting, Strings
Date       : 2026-10-02

Approach:
    Rearrange the digits of A and B so that, position by position,
    max(a_i, b_i) forms the largest possible lucky string (only 4s and 7s).
    - A position gives '7' if both digits are <= 7 and at least one is 7.
    - A position gives '4' if both digits are <= 4 and at least one is 4.
    Greedy: first maximise the number of 7s (k = min(#<=7 in A, #<=7 in B,
    #7s in A + #7s in B)). Fill the unmatched side of each 7-pair with the
    "cheapest" digits (5/6 first, then 0-3, then 4 last), so the digits <= 4
    needed for the 4s are preserved. Then count how many 4s can still be
    formed from the leftover digits. Output is '7'*k + '4'*k4.

Time  : O(N) per test case (single counting pass over each string)
Space : O(1) extra, apart from the output string
"""


# -------------------------------------- Solution ---------------------------------------------------------


import sys

def get_counts(s):
    return (
        s.count('7'),
        sum(c <= '7' for c in s),
        sum(c in '56' for c in s),
        sum(c <= '4' for c in s),
        s.count('4'),
        sum(c in '0123' for c in s),
    )

def solve(A, B):
    sA, le7A, midA, qA, fA, lowA = get_counts(A)
    sB, le7B, midB, qB, fB, lowB = get_counts(B)
    k = min(le7A, le7B, sA + sB)
    useA7 = min(sA, k)
    useB7 = min(sB, k)
    needA = k - useA7
    needB = k - useB7
    low_consume_A = max(0, needA - midA)
    low_consume_B = max(0, needB - midB)
    rem_qA = qA - low_consume_A
    rem_qB = qB - low_consume_B
    consumed_4_A = max(0, low_consume_A - lowA)
    consumed_4_B = max(0, low_consume_B - lowB)
    rem_fA = fA - consumed_4_A
    rem_fB = fB - consumed_4_B
    k4 = min(rem_qA, rem_qB, rem_fA + rem_fB)
    return '7' * k + '4' * k4

def main():
    input = sys.stdin.readline
    T = int(input())
    ans = []
    for _ in range(T):
        A = input().strip()
        B = input().strip()
        ans.append(solve(A, B))
    sys.stdout.write('\n'.join(ans))

if __name__ == "__main__":
    main()
