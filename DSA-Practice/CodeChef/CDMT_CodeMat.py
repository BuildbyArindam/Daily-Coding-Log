# Problem: CodeMat
# Platform: CodeChef
# Link: https://www.codechef.com/problems/CDMT
# Date Solved: 2026-08-26
# Approach: Read two integers x, y. Print "YES" if y > x, else "NO" —
#           a single direct comparison, no preprocessing needed.
# Time Complexity: O(1)
# Space Complexity: O(1)


# ------------------------- Solution ----------------------------

x, y = map(int, input().split())
if y > x:
    print("YES")
else:
    print("NO")
