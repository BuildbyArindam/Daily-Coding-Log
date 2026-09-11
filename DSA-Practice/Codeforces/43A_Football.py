"""
Problem   : Football
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/43/A
Date      : 2026-09-11
Difficulty: *1000
Topic     : Strings

Approach:
Read n lines, each naming the team that scored a goal. Tally goals per
team in a dict. The problem guarantees exactly one team scored strictly
more than half the total goals, so the team with the max count is
always the correct winner (max() over the dict values is sufficient
here — no explicit >n/2 check needed given the guarantee).

Time Complexity : O(n)   - one pass over n inputs, dict get/set is O(1) amortized
Space Complexity: O(k)   - k = number of distinct team names (at most 2 by constraints)
"""


# --------------------------- Solution --------------------------------


n = int(input())

teams = {}
for _ in range(n):
    team = input().strip()
    teams[team] = teams.get(team, 0) + 1
winner = max(teams, key=teams.get)
print(winner)
