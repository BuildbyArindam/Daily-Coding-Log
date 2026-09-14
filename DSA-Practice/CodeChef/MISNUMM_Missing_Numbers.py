"""
Problem   : Missing Numbers
Platform  : CodeChef
Link      : https://www.codechef.com/DSAMONDAY020/problems/MISNUMM
Date      : 2026-09-14
Difficulty: Easy 
Topics    : Hashing / Frequency Counting, Arrays, Sorting

Approach:
  Count frequency of each value in array A and array B using Counter.
  For every distinct value in B, compare its count in B against its
  count in A. If B needs more occurrences of that value than A has,
  it's a "missing number" — collect it, sort, and print. If none
  found, print -1.

Time Complexity  : O(n + m + k log k), where n = len(A), m = len(B),
                    k = number of distinct missing values (from final sort)
Space Complexity : O(n + m) for the two frequency counters
"""


# ------------------------- Solution -----------------------------------------


import sys
from collections import Counter as _C

def _grab_ints(line):
    return list(map(int, line.split()))

def main():
    data = sys.stdin.read().split('\n')
    idx = 0
    n_len = int(data[idx].strip()); idx += 1
    arr_a = _grab_ints(data[idx]); idx += 1
    m_len = int(data[idx].strip()); idx += 1
    arr_b = _grab_ints(data[idx]); idx += 1
    freq_a = _C(arr_a)
    freq_b = _C(arr_b)
    result_set = []
    for val in freq_b:
        cnt_in_b = freq_b[val]
        cnt_in_a = freq_a.get(val, 0)
        if cnt_in_a < cnt_in_b:
            result_set.append(val)
    if not result_set:
        print(-1)
    else:
        result_set.sort()
        print(' '.join(str(x) for x in result_set))

if __name__ == '__main__':
    main()
