"""
Problem: Changing Money
Platform: CodeChef
Link: https://www.codechef.com/practice/course/icpc/ICPCTR08/problems/KAN13G
Date Solved: 2026-09-27
Difficulty: Medium
Topics: Greedy, Simulation, String Parsing

Approach:
Parse currency denominations and owed amounts into integer paisa (avoiding
floating point errors). For each scenario, greedily break down the owed
amount using denominations sorted in descending order, using divmod to
find how many of each denomination are needed. Convert paisa values back
to a clean decimal string label for output.

Time Complexity: O(D log D + S * D) per test case
  - D = number of denominations, S = number of scenarios
  - D log D for sorting denominations, D per scenario for greedy breakdown
Space Complexity: O(D) for storing denominations
"""


# ----------------------------------- Solution -----------------------------------------------


import sys

def to_paisa(token):
    token = token.strip()
    if "." in token:
        whole_part, frac_part = token.split(".")
        frac_part = (frac_part + "00")[:2]
    else:
        whole_part, frac_part = token, "00"
    whole_part = whole_part if whole_part else "0"
    return int(whole_part) * 100 + int(frac_part)

def paisa_to_label(value):
    units, sub = divmod(value, 100)
    if sub == 0:
        return str(units)
    return "{}.{:02d}".format(units, sub)

def greedy_breakdown(owed, denom_list_desc):
    left = owed
    for denom in denom_list_desc:
        if left <= 0:
            break
        used, left = divmod(left, denom)
        if used:
            yield denom, used

def run():
    tokens = sys.stdin.read().split()
    cursor = [0]
    def next_token():
        tok = tokens[cursor[0]]
        cursor[0] += 1
        return tok
    total_cases = int(next_token())
    output_chunks = []
    for case_no in range(1, total_cases + 1):
        num_denoms = int(next_token())
        num_scenarios = int(next_token())
        raw_denoms = [next_token() for _ in range(num_denoms)]
        denoms_paisa = sorted((to_paisa(tok) for tok in raw_denoms), reverse=True)
        output_chunks.append("Case {}:".format(case_no))
        for scenario_no in range(1, num_scenarios + 1):
            owed_paisa = to_paisa(next_token())
            output_chunks.append("Scenario {}:".format(scenario_no))
            for denom_paisa, count in greedy_breakdown(owed_paisa, denoms_paisa):
                output_chunks.append(
                    "{} {}".format(paisa_to_label(denom_paisa), count)
                )
    sys.stdout.write("\n".join(output_chunks) + "\n")

if __name__ == "__main__":
    run()
