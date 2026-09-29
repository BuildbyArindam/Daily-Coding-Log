"""
Problem   : Trail Sensor Watch
Platform  : Unstop
Link      : https://unstop.com/code/practice/661272
Difficulty: Medium
Date      : 2026-09-29
Topics    : Sliding Window, Hashing, Frequency Counting, Monotonic Queue, Array

Approach:
    Slide a window of size k over the readings. Two structures are maintained:
      - A frequency map of species IDs in the window, so the number of
        distinct species is len(freq).
      - A monotonic decreasing deque of indices, so the window maximum
        is always v[dq[0]].
    For each full window, if 2 * distinct_species >= k, output the window
    max; otherwise output -1. Then evict the outgoing element from the
    frequency map.

Complexity:
    Time : O(n) - each index is pushed/popped from the deque at most once,
           and each map update is O(1) average.
    Space: O(k) auxiliary for the deque and frequency map
           (O(n) including input and output arrays).
"""


# ------------------------------------ Solution ------------------------------------------------


def compute_notable_readings(n, k, v, s):
    from collections import defaultdict, deque
    freq = defaultdict(int)
    dq = deque()
    result = []
    for i in range(n):
        freq[s[i]] += 1
        while dq and v[dq[-1]] <= v[i]:
            dq.pop()
        dq.append(i)
        left = i - k + 1
        if dq and dq[0] < left:
            dq.popleft()
        if i >= k - 1:
            distinct_species = len(freq)
            if 2 * distinct_species >= k:
                result.append(v[dq[0]])
            else:
                result.append(-1)
            outgoing = i - k + 1
            freq[s[outgoing]] -= 1
            if freq[s[outgoing]] == 0:
                del freq[s[outgoing]]
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])  
    k = int(data[1]) 
    v = list(map(int, data[2:n+2])) 
    s = list(map(int, data[n+2:2*n+2])) 
    result = compute_notable_readings(n, k, v, s)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
