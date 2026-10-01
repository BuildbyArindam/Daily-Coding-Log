"""
Platform   : CodeChef
Problem    : Codechef Copy (CC_COPY)
Link       : https://www.codechef.com/problems/CC_COPY
Difficulty : 1718
Topics     : Number System, Mathematics
Date       : 2026-10-01

Approach:
    Rearrange the characters of s into a new 8-character string so that no
    position matches "codechef". Backtracking fills positions left to right,
    trying the most frequent remaining character first. Before each step, a
    feasibility check prunes dead branches: every character's remaining count
    must be <= the number of remaining positions where the target differs
    from that character. If no valid arrangement exists, print -1.

Complexity:
    Time  : O(T * k * 8) in practice, where k = distinct chars (<= 8).
            Worst-case O(8!) per test, but the pruning avoids it, and the
            length is fixed at 8, so it is O(1) per test.
    Space : O(1), since the recursion depth and arrays are bounded by 8.
"""


# ------------------------------- Solution ----------------------------------------------


T = int(input())
target = "codechef"

for _ in range(T):
    s = input().strip()
    chars = list(set(s))
    counts = {ch: s.count(ch) for ch in chars}
    ans = [""] * 8
    def possible(pos):
        for ch in chars:
            need = counts[ch]
            if need == 0:
                continue
            allowed = 0
            for i in range(pos, 8):
                if target[i] != ch:
                    allowed += 1
            if need > allowed:
                return False
        return True

    def dfs(pos):
        if pos == 8:
            return True
        if not possible(pos):
            return False
        order = sorted(chars, key=lambda ch: -counts[ch])
        for ch in order:
            if counts[ch] == 0:
                continue
            if ch == target[pos]:
                continue
            counts[ch] -= 1
            ans[pos] = ch
            if dfs(pos + 1):
                return True
            counts[ch] += 1
        return False
    if dfs(0):
        print("".join(ans))
    else:
        print(-1)
