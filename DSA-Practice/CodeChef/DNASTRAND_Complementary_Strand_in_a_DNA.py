# ------------------------------------------------------------------
# Problem   : Complementary Strand in a DNA
# Platform  : CodeChef
# Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DNASTRAND
# Difficulty: 660
# Topics    : String Manipulation, Hashing, Basic Programming
# Date      : 2026-09-19
#
# Approach:
#   For each character in the DNA string, map it to its Watson-Crick
#   complement (A<->T, C<->G) using simple conditional checks, and
#   build the complementary strand character by character.
#
# Time Complexity : O(N) per test case, where N = len(S)
# Space Complexity : O(N) for the complement string
# ------------------------------------------------------------------


# ----------------------------------- Solution ----------------------------------------


T = int(input())

for _ in range(T):
    N = int(input())
    S = input()
    complement = ""
    for ch in S:
        if ch == 'A':
            complement += 'T'
        elif ch == 'T':
            complement += 'A'
        elif ch == 'C':
            complement += 'G'
        elif ch == 'G':
            complement += 'C'
    print(complement)
