"""
Problem   : Container Merge Line
Platform  : Unstop
Link      : https://unstop.com/code/practice/656218
Difficulty: Medium
Topic     : Stack, Simulation

Date      : 2026-08-19

Approach:
    Simulate placing containers on a line, left to right. Push each new
    weight onto a stack. Whenever the top two elements are equal, merge
    them into a single container of double the weight (pop + update top),
    and keep checking — a merge can cascade if it creates a new equal
    pair with the element below it. This mirrors "2048-style" merging.

Time Complexity : O(n) amortized
    - Each element is pushed once and popped at most once overall,
      so the total work across all merges is bounded by n.

Space Complexity: O(n)
    - Stack holds at most n elements in the worst case (no merges).
"""


# ------------------------ Solution ---------------------------


n = int(input())
weights = list(map(int, input().split()))
stack = []
for w in weights:
    stack.append(w)
    while len(stack) >= 2 and stack[-1] == stack[-2]:
        merged = stack.pop() * 2
        stack[-1] = merged
print(len(stack))
print(*stack)
