"""
Problem   : Maximum Size Rectangle Sub-matrix With All 1's
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/maximum-size-rectangle-sub-matrix-with-all-1-s_893017
Difficulty: Hard
Date      : 2026-08-23

Approach:
Treat each row of the binary matrix as the base of a histogram, where
heights[j] = number of consecutive 1's ending at the current row in column j
(reset to 0 whenever a 0 is encountered). For every row, run the classic
"Largest Rectangle in Histogram" algorithm using a monotonic increasing
stack of indices to find the max rectangle area with that row as the base.
Track the running maximum across all rows.

Time Complexity : O(N * M)   -- each cell pushed/popped from the stack at most once per row
Space Complexity: O(M)       -- heights array + stack
"""


# ------------------------------ Solution ----------------------------------


from sys import stdin, stdout, setrecursionlimit

def maximalAreaOfSubMatrix(mat, N, M):
    heights = [0] * M
    max_area = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0
        stack = [-1]
        for j in range(M + 1):
            current_height = 0 if j == M else heights[j]
            while stack[-1] != -1 and heights[stack[-1]] > current_height:
                h = heights[stack.pop()]
                width = j - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(j)
    return max_area

def takeInput():
    N, M = list(map(int, stdin.readline().strip().split(" ")))
    mat = list()
    for i in range(N):
        mat.append(list(map(int, stdin.readline().strip().split(" "))))
    return N, M, mat

tc = int(input())
while tc > 0:
    N, M, mat = takeInput()
    ans = maximalAreaOfSubMatrix(mat, N, M)
    stdout.write(str(ans) + "\n")
    tc -= 1
