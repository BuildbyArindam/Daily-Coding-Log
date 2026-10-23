"""
Problem   : Guess It Right (GUESSRT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GUESSRT
Difficulty: 2012
Solved on : 2026-10-23
Topics    : Probability, Modular Arithmetic, Exponentiation, Number Theory

Approach:
    Compute the probability of never guessing correctly, then answer 1 - that.
    - Each of the ceil(moves / 2) rounds fails with probability (1 - 1/boxes),
      so the all-fail probability is (1 - 1/boxes)^rounds.
    - If moves is even, there is one extra trailing attempt that fails with
      probability (1 - 1/(boxes + step)), so multiply that in.
    - All probabilities are handled as modular inverses under MOD = 1e9+7
      (Fermat's little theorem), with fast exponentiation via pow().

Complexity:
    Time : O(T * log MOD), a few modular exponentiations per test case
    Space: O(T) for buffered output (O(1) extra per test case)
"""


# ------------------------------------------- Solution ------------------------------------------------------


import sys

def main():
    MOD = 10**9 + 7
    raw = sys.stdin.buffer.read().split()
    cases = int(raw[0])
    out = []
    pos = 1
    for _ in range(cases):
        boxes = int(raw[pos]); step = int(raw[pos + 1]); moves = int(raw[pos + 2])
        pos += 3
        inv_boxes = pow(boxes, MOD - 2, MOD)
        miss = (1 - inv_boxes) % MOD      
        rounds = (moves + 1) >> 1       
        lose = pow(miss, rounds, MOD)
        if moves % 2 == 0:
            lose = lose * ((1 - pow(boxes + step, MOD - 2, MOD)) % MOD) % MOD
        out.append((1 - lose) % MOD)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
