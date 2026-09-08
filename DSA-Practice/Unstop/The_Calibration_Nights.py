"""
Problem   : The Calibration Nights
Platform  : Unstop
Link      : https://unstop.com/code/practice/659275
Difficulty: Hard
Date      : 2026-09-08
Topics    : Dynamic Programming, Convex Hull Trick (CHT), DP Optimization, Math

Approach:
dp[i] = min over j < i of ( dp[j] + w*(i-j)^2 ) + energy[i]
Expand the quadratic: w*(i-j)^2 = w*i^2 - 2*w*i*j + w*j^2
=> for each j, this is a line in x=i: y = m*x + b, where m = -2*w*j, b = dp[j] + w*j^2
Since both the query point x=i and each new line's slope m are monotonic as i
increases, maintain a monotonic Convex Hull Trick (CHT) deque:
  - a 'head' pointer that only moves forward for queries (min at x=i)
  - pop from the back when the new line makes the second-to-last line obsolete
    (standard bad-line check via cross-multiplication to avoid floating point)

Time Complexity : O(n) amortized — monotonic CHT, both head and tail pointers
                  each move forward at most n times total
Space Complexity: O(n) — dp array + lines deque
"""


# ------------------------ Solution ------------------------


n, w = map(int, input().split())
energy = list(map(int, input().split()))
dp = [0] * n
lines = []
def value(line, x):
    m, b = line
    return m * x + b
dp[0] = energy[0]
j = 1
lines.append((-2 * w * j, dp[0] + w * j * j))
head = 0
for i in range(2, n + 1):
    x = i
    while head + 1 < len(lines) and value(lines[head], x) >= value(lines[head + 1], x):
        head += 1
    best = value(lines[head], x)
    dp[i - 1] = energy[i - 1] + w * x * x + best
    m = -2 * w * i
    b = dp[i - 1] + w * i * i
    new_line = (m, b)
    while len(lines) - head >= 2:
        m1, b1 = lines[-2]
        m2, b2 = lines[-1]
        m3, b3 = new_line
        if (b2 - b1) * (m2 - m3) >= (b3 - b2) * (m1 - m2):
            lines.pop()
        else:
            break
    lines.append(new_line)
print(dp[n - 1])
