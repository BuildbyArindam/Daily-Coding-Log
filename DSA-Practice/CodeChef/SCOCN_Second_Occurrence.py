"""
Problem: Second Occurrence
Platform: CodeChef
Link: https://www.codechef.com/problems/SCOCN
Date: 2026-09-01
Difficulty: Cakewalk
Topics: Arrays, Linear Search, Basic Implementation
Approach: Single left-to-right scan tracking occurrence count of X.
          Print index (0-based) of the 2nd occurrence if found;
          -1 if X never occurs; -2 if X occurs exactly once.
Time Complexity: O(N)
Space Complexity: O(N) for storing the array (O(1) extra)
"""


# ------------------------- Solution --------------------------------


N = int(input())
A = list(map(int, input().split()))
X = int(input())
count = 0
for i in range(N):
    if A[i] == X:
        count += 1
        if count == 2:
            print(i)
            break
else:
    if count == 0:
        print(-1)
    else:
        print(-2)
