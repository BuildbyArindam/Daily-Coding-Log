"""
Problem   : Shuffle (Hard) - CodeChef START258B (SHUFFLEHD)
Link      : https://www.codechef.com/START258B/problems/SHUFFLEHD
Date      : 2026-09-30
Platform  : CodeChef
Difficulty: Hard
Topics    : Monotonic Stack, Combinatorics

Approach:
  Maintain a monotonic (decreasing) stack of indices. For each position i,
  find the nearest previous index whose value is greater than arr[i].
  The number of valid placements for i is the difference between the
  window capacities at i and at that previous index (+1), where capacity
  at index j is min(K, N - j + 1). Multiply these counts together modulo
  998244353. If any count is <= 0, the answer is 0.

Complexity:
  Time : O(N) per test case (each index is pushed and popped at most once)
  Space: O(N) for the stack and input array
"""


# ----------------------------------------- Solution ------------------------------------------------


import sys
MOD_VAL = 998244353

def _tail_capacity(total_len, k_val, idx):
    remain = total_len - idx + 1
    return k_val if remain >= k_val else remain

def _process_case(total_len, k_val, arr):
    stack_idx = []
    running = 1
    for cur_pos in range(1, total_len + 1):
        cur_val = arr[cur_pos - 1]
        while stack_idx and arr[stack_idx[-1] - 1] <= cur_val:
            stack_idx.pop()
        prev_idx = stack_idx[-1] if stack_idx else 0
        cap_here = _tail_capacity(total_len, k_val, cur_pos)
        cap_prev = 1 if prev_idx == 0 else _tail_capacity(total_len, k_val, prev_idx)
        gap = cap_here - cap_prev + 1
        if gap <= 0:
            return 0
        running = (running * gap) % MOD_VAL
        stack_idx.append(cur_pos)
    return running

def main():
    raw = sys.stdin.buffer.read().split()
    ptr = 0
    t_count = int(raw[ptr]); ptr += 1
    answers = []
    for _ in range(t_count):
        n_val = int(raw[ptr]); k_val = int(raw[ptr + 1]); ptr += 2
        q_arr = list(map(int, raw[ptr:ptr + n_val])); ptr += n_val
        answers.append(str(_process_case(n_val, k_val, q_arr)))
    sys.stdout.write('\n'.join(answers) + '\n')

if __name__ == "__main__":
    main()
