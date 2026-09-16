"""
Problem   : Transfer
Platform  : CodeChef (START256D)
Link      : https://www.codechef.com/START256D/problems/TRANSFER
Date      : 2026-09-16
Difficulty: Hard 
Topics    : Greedy, Stack, Isotonic Regression / PAV, Math

Approach:
    Process the array left to right, maintaining a stack of "blocks"
    (sum, count). Each new element starts its own block; while the
    average of the second-to-last block exceeds the average of the
    last block (a violation of non-decreasing order), merge them.
    This is the Pool Adjacent Violators algorithm, producing the
    closest non-decreasing sequence to `values` under L1/L2-style
    leveling. Each merged block is then leveled to as-equal-as-possible
    integer values (quotient/remainder split) to reconstruct the
    target sequence, and the total answer is accumulated using each
    element's original value, its leveled target, and its distance
    from the end of the array (positional weight).

Time complexity : O(n) amortized per test case — each element is
                   pushed and merged into the stack at most once.
Space complexity : O(n) for the block stack.
"""


# ------------------------------- Solution --------------------------------


import sys

def transfers(values):
    groups = []
    for value in values:
        groups.append([value, 1])
        while len(groups) >= 2:
            s_left, n_left = groups[-2]
            s_right, n_right = groups[-1]
            highest_left = (s_left + n_left - 1) // n_left
            lowest_right = s_right // n_right
            if highest_left <= lowest_right:
                break
            groups.pop()
            groups.pop()
            groups.append([s_left + s_right, n_left + n_right])
    total = 0
    pos = 0
    length = len(values)
    for block_sum, block_len in groups:
        quotient, remainder = divmod(block_sum, block_len)
        for j in range(block_len):
            final_value = quotient if j < block_len - remainder else quotient + 1
            total += (values[pos] - final_value) * (length - 1 - pos)
            pos += 1
    return total

def main():
    input_data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    test_cases = input_data[ptr]
    ptr += 1
    answers = []
    for _ in range(test_cases):
        n = input_data[ptr]
        ptr += 1
        arr = input_data[ptr:ptr + n]
        ptr += n
        answers.append(str(transfers(arr)))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
