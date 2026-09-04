"""
Problem   : Smart Boy
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/38/F
Difficulty: *2100
Topics    : DP, Games, Strings
Date      : 2026-09-04

Approach:
    Every distinct substring across all dictionary words is a game
    "state". From state s, a move appends one character (left or
    right) to reach a longer substring t, provided t also occurs in
    some dictionary word. score(s) = cnt(s) + max_letter(s) * sum(s),
    where cnt(s) counts distinct words containing s.

    Process states in decreasing order of length (longest first, since
    those have no outgoing moves and are the DP base case). For each
    state u, dp[u] = (best achievable score for the player to move,
    opponent's resulting score) under optimal play, where a player
    first maximizes whether they win (i.e. forces the opponent into a
    state with no moves), then maximizes their own score, then
    minimizes the opponent's score. Transitions flip perspective:
    moving u -> v means the mover immediately banks score[v], and
    dp[v] = (next player's score, mover's carried-over score) is
    reinterpreted from the mover's point of view.

    The actual game starts with the first player picking any single
    letter as the initial substring, so the answer is obtained by
    running the same "best" comparison over all length-1 states.

Complexity:
    Let S = total length of all dictionary words (n <= 5, |word| <= 4000
    per the problem's original constraints, so S is small in practice,
    but bounding generally): there are O(S^2) distinct substrings in
    the worst case (all l..r pairs per word), each with O(1) outgoing
    edges (left-extend, right-extend), so:
        Time : O(S^2) to build states/graph + O(S^2) for the DP pass
               (each state visited once, O(1) work per outgoing edge
               beyond the edge set itself)
        Space: O(S^2) for storing all distinct substrings, the
               id_of map, the graph adjacency, cnt[], score[], dp[]
"""


# -------------------------- Solution -------------------------------


import sys

input = sys.stdin.readline
def solve():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    id_of = {}
    strings = []
    graph = []
    cnt = []
    def get_id(s):
        if s not in id_of:
            idx = len(strings)
            id_of[s] = idx
            strings.append(s)
            graph.append(set())
            cnt.append(0)
        return id_of[s]
    for w in words:
        m = len(w)
        seen = set()
        for l in range(m):
            for r in range(l, m):
                s = w[l:r + 1]
                u = get_id(s)
                seen.add(u)
                if l > 0:
                    v = get_id(w[l - 1:r + 1])
                    graph[u].add(v)
                if r + 1 < m:
                    v = get_id(w[l:r + 2])
                    graph[u].add(v)
        for u in seen:
            cnt[u] += 1
    states = len(strings)
    score = [0] * states
    for u, s in enumerate(strings):
        total = 0
        maximum = 0
        for ch in s:
            x = ord(ch) - ord('a') + 1
            total += x
            if x > maximum:
                maximum = x
        score[u] = cnt[u] + total * maximum
    order = sorted(range(states), key=lambda u: len(strings[u]),
                   reverse=True)
    win = [False] * states
    dp = [(0, 0)] * states
    def better(a, b):
        """
        Is outcome a better for the current player than outcome b?

        First maximize own score.
        If tied, minimize opponent score.
        """
        if a[0] != b[0]:
            return a[0] > b[0]
        return a[1] < b[1]
    for u in order:
        if not graph[u]:
            win[u] = False
            dp[u] = (0, 0)
            continue
        best = None
        best_win = False
        for v in graph[u]:
            a, b = dp[v]
            candidate = (score[v] + b, a)
            candidate_win = not win[v]
            if best is None:
                best = candidate
                best_win = candidate_win
                continue
            if candidate_win != best_win:
                if candidate_win:
                    best = candidate
                    best_win = True
            elif better(candidate, best):
                best = candidate
                best_win = candidate_win
        win[u] = best_win
        dp[u] = best
    best = None
    first_wins = False
    for v, s in enumerate(strings):
        if len(s) != 1:
            continue
        a, b = dp[v]
        candidate = (score[v] + b, a)
        candidate_win = not win[v]
        if best is None:
            best = candidate
            first_wins = candidate_win
            continue
        if candidate_win != first_wins:
            if candidate_win:
                best = candidate
                first_wins = True
        elif better(candidate, best):
            best = candidate
            first_wins = candidate_win
    print("First" if first_wins else "Second")
    print(best[0], best[1])

if __name__ == "__main__":
    solve()
