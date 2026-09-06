"""
Problem: Chess Tournament
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/chess-tournament-4/
Difficulty: Easy
Topics: Basic Programming, Implementation

Date: 2026-09-06

Approach:
    2^N players compete in a single-elimination bracket. A lower-triangular
    match matrix A tells us, for any pair (i, j) with i > j, whether player i
    beats player j (A[i-2][j-1] == 1) or loses. Simulate the bracket round by
    round: pair up adjacent players in the current round, resolve each match
    with winner(), and carry the winners forward until one player remains.

Time Complexity:  O(2^N)   -> each of the (players - 1) matches is resolved once
Space Complexity: O(2^N)   -> storage for the match matrix A and the round arrays
"""


# --------------------------- Solution ----------------------------------


name = input()
N = int(name)
players = 2 ** N
A = []
for i in range(1, players):
    A.append(bytearray(map(int, input().split())))

def winner(i, j):
    """
    Return the better player between participants i and j.
    Participant IDs are 1-based.
    """
    if i > j:
        if A[i - 2][j - 1] == 1:
            return i
        else:
            return j
    else:
        if A[j - 2][i - 1] == 1:
            return j
        else:
            return i

current = list(range(1, players + 1))
while len(current) > 1:
    next_round = []
    for i in range(0, len(current), 2):
        w = winner(current[i], current[i + 1])
        next_round.append(w)
    current = next_round
print(current[0])
