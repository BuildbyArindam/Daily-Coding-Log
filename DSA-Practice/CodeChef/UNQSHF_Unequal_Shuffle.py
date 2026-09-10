"""
Problem   : Unequal Shuffle (UNQSHF)
Link      : https://www.codechef.com/problems/UNQSHF
Date      : 2026-09-10
Platform  : CodeChef
Difficulty: 800–1000 (Easy) 
Topics: Combinatorics, Greedy, Math, Counting/Frequency, String Manipulation

Approach:
    Let a1 = count of 'a' in A, a2 = count of 'a' in B (N = length of each string).
    Since both strings can be freely rearranged, a valid assignment with
    A[i] != B[i] for all i exists iff every 'a' in A can be paired with a
    'b' in B and every 'b' in A paired with an 'a' in B. Working out the
    two inequalities (a1 <= N-a2 and N-a1 <= a2) shows both hold
    simultaneously only when a1 + a2 == N exactly.

Time Complexity  : O(N) per test case  ->  O(sum of N) overall
Space Complexity : O(N) for input strings, O(1) extra
"""





T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()
    if A.count('a') + B.count('a') == N:
        print("YES")
    else:
        print("NO")
