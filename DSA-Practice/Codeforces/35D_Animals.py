"""
Problem   : 35D - Animals
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/35/D
Difficulty: *1700
Tags      : dp, greedy

Approach:
    Each animal arriving on day i (1-indexed) eats c[i] tons/day from
    day i through day n, so its total lifetime cost is c[i] * (n - i + 1).
    To maximize the COUNT of animals kept (not minimize cost), it's always
    optimal to prefer cheaper total-cost animals first — sort all n costs
    ascending and greedily take from the cheapest up until the food X
    runs out. This greedy is optimal because with a fixed budget X, taking
    the k smallest-cost items maximizes the number of items you can afford
    (standard exchange argument: swapping a costlier chosen item for a
    cheaper unchosen one never increases total cost).

Time complexity : O(n log n)   -- dominated by the sort
Space complexity: O(n)         -- storing the costs array
"""


# --------------------------- Solution --------------------------------


with open("input.txt", "r") as f:
    data = list(map(int, f.read().split()))
n = data[0]
X = data[1]
c = data[2:]
costs = []
for i in range(n):
    days = n - i
    costs.append(c[i] * days)
costs.sort()
count = 0
for cost in costs:
    if X >= cost:
        X -= cost
        count += 1
    else:
        break

with open("output.txt", "w") as f:
    f.write(str(count))
