"""
Problem: Max Stack
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/max-stack_985280?kunjiRedirection=true
Date: 2026-08-22
Difficulty: Easy
Topic: Stack, Design

Approach:
Maintain two stacks — `stack` holds the actual pushed values, and `max_stack`
is an auxiliary stack where max_stack[i] always stores the max value among
stack[0..i]. On push, we push max(new_value, current_max) onto max_stack,
so the top of max_stack is always the running max in O(1). Pop/top/max all
just read/mutate the tops of these two stacks in sync.

Time Complexity:  O(1) for specialPush, specialPop, specialTop, specialMax
Space Complexity: O(n) — extra max_stack of same size as stack
"""


# -------------------------- Solution -----------------------------


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def specialPush(self, value):
        self.stack.append(value)
        if not self.max_stack:
            self.max_stack.append(value)
        else:
            self.max_stack.append(max(value, self.max_stack[-1]))

    def specialPop(self):
        if not self.stack:
            return -1
        self.max_stack.pop()
        return self.stack.pop()

    def specialTop(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def specialMax(self):
        if not self.stack:
            return -1
        return self.max_stack[-1]
