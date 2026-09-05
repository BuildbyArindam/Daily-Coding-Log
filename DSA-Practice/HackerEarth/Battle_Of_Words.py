"""
Problem: Battle Of Words
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/battle-of-words/
Difficulty: Easy
Topics: Ad-Hoc, Basic Programming, Implementation

Date Solved: 2026-09-05

Approach:
Strip spaces from both strings and build 26-length frequency counts for
each. Cancel out matching character counts between the two strings
(each shared letter can "kill" one occurrence from each side). Whichever
string still has leftover (uncancelled) letters "wins" that string's
side — if only A has leftovers, A survived (win); if only B has
leftovers, B survived (lose, since we're comparing from A's perspective);
if both or neither have leftovers, it's a draw.

Time Complexity: O(N + M) per test case, where N, M are string lengths
                  (26-size array operations are O(1))
Space Complexity: O(1) — fixed-size 26-length count arrays
"""


# --------------------------- Solution ---------------------------------


name = input()
T = int(name)
for _ in range(T):
    a = input().strip().replace(' ', '')
    b = input().strip().replace(' ', '')
    count_a = [0] * 26
    count_b = [0] * 26
    for ch in a:
        count_a[ord(ch) - ord('a')] += 1
    for ch in b:
        count_b[ord(ch) - ord('a')] += 1
    for i in range(26):
        common = min(count_a[i], count_b[i])
        count_a[i] -= common
        count_b[i] -= common
    a_alive = any(count_a)
    b_alive = any(count_b)
    if a_alive and not b_alive:
        print("You win some.")
    elif b_alive and not a_alive:
        print("You lose some.")
    else:
        print("You draw some.")
