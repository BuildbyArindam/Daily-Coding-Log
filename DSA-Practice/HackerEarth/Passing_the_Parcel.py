"""
Problem: Passing the Parcel
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/passing-the-parcel/
Date Solved: 2026-09-06
Difficulty: Easy
Topics: Ad-Hoc, Brute-force search, Implementation

Approach:
Simulate the "passing the parcel" game directly. Maintain a list of
remaining students and a pointer `current` for who holds the parcel.
Walk through the song string character by character (cyclically):
  - 'a' -> advance the parcel to the next student (mod current length)
  - anything else -> that student is eliminated; remove them from the
    list and clamp `current` back into range
Repeat until only one student remains; print them.

Time Complexity:  O(N * L) worst case, where N = number of students and
                   L = len(S) — each elimination can take up to O(N) for
                   the list.pop(), and we do this N-1 times, plus O(L)
                   song traversal steps between eliminations in the
                   worst case (bounded overall by total steps needed).
Space Complexity: O(N) for the students list.
"""


# --------------------------- Solution -------------------------------


N = int(input())
S = input().strip()
students = list(range(1, N + 1))
current = 0  
song_pos = 0   
while len(students) > 1:
    ch = S[song_pos]
    if ch == 'a':
        current = (current + 1) % len(students)
    else: 
        students.pop(current)
        if len(students) > 0:
            current %= len(students)
    song_pos = (song_pos + 1) % len(S)
print(students[0])
