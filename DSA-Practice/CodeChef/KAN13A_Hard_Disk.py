"""
Problem   : Hard Disk (ICPCTR08 / KAN13A)
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/icpc/ICPCTR08/problems/KAN13A
Date      : 2026-09-27
Difficulty: Hard
Topics    : DP, Greedy-swap, Path Reconstruction

Approach:
For each month, choose a disk kind to hold. Switching kinds costs a
flat Tk 100 penalty. running_best[k] tracks the minimum total cost to
be holding kind k at the current month (paying the switch penalty the
last time the kind changed), with running_from[k] recording the month
that run started. Each month, find the cheapest kind to switch from
(swap_value), then extend every kind's running cost from that swap
plus this month's price (+100 switch fee). Track the global best
(champion_cost/month/kind) seen at every step, then walk back_month /
back_kind pointers from the champion to reconstruct the full sequence
of (start_month, kind) segments.

Time complexity : O(horizon * disk_kinds) per test case
Space complexity: O(disk_kinds + horizon) per test case
"""


# ------------------------------------ Solution ----------------------------------------


import sys

def read_all_tokens():
    return sys.stdin.read().split()

def process_case(tok, pos):
    case_label = tok[pos]; pos += 1
    disk_kinds = int(tok[pos]); pos += 1
    horizon = int(tok[pos]); pos += 1
    labels = []
    price_grid = []
    for _ in range(disk_kinds):
        labels.append(tok[pos]); pos += 1
        row = [int(tok[pos + j]) for j in range(horizon)]
        pos += horizon
        price_grid.append(row)
    INF = float('inf')
    running_best = [INF] * disk_kinds
    running_from = [0] * disk_kinds
    back_month = [0] * (horizon + 1)
    back_kind = [0] * (horizon + 1)
    champion_cost = INF
    champion_month = 1
    champion_kind = 0
    this_month_cost = [price_grid[k][0] for k in range(disk_kinds)]
    for k, c in enumerate(this_month_cost):
        if c < champion_cost:
            champion_cost, champion_month, champion_kind = c, 1, k
    for k, c in enumerate(this_month_cost):
        if c < running_best[k]:
            running_best[k] = c
            running_from[k] = 1
    for month in range(2, horizon + 1):
        col = month - 1 
        swap_value = INF
        swap_source_kind = -1
        for k in range(disk_kinds):
            candidate = running_best[k] - price_grid[k][col]
            if candidate < swap_value:
                swap_value = candidate
                swap_source_kind = k
        back_month[month] = running_from[swap_source_kind]
        back_kind[month] = swap_source_kind
        this_month_cost = [swap_value + price_grid[k][col] + 100 for k in range(disk_kinds)]
        for k, c in enumerate(this_month_cost):
            if c < champion_cost:
                champion_cost, champion_month, champion_kind = c, month, k
        for k, c in enumerate(this_month_cost):
            if c < running_best[k]:
                running_best[k] = c
                running_from[k] = month
    chain = []
    a, k = champion_month, champion_kind
    while True:
        chain.append((a, k))
        if a == 1:
            break
        a, k = back_month[a], back_kind[a]
    chain.reverse()
    lines = [case_label, "Tk %d" % champion_cost]
    for i, (start_month, kind_idx) in enumerate(chain):
        if i + 1 < len(chain):
            end_month = chain[i + 1][0] - 1
        else:
            end_month = horizon
        span = end_month - start_month + 1
        lines.append("%s for %d month(s)" % (labels[kind_idx], span))
    lines.append("")
    return lines, pos

def main():
    tok = read_all_tokens()
    pos = 0
    all_lines = []
    while tok[pos] != "TheEnd":
        lines, pos = process_case(tok, pos)
        all_lines.extend(lines)
    all_lines.append("TheEnd")
    sys.stdout.write("\n".join(all_lines) + "\n")

if __name__ == "__main__":
    main()
