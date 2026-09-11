"""
Problem   : Tara's Interference Window
Platform  : Unstop
Link      : https://unstop.com/code/practice/659655
Difficulty: Hard
Topics    : Array, Prefix XOR, Trie (Binary Trie), Sliding Window, Bit Manipulation
Date      : 2026-09-11

Approach:
    - Build prefix XOR array P[0..n], where P[i] = w[1] ^ w[2] ^ ... ^ w[i].
      Any subarray XOR w[l+1..r] = P[r] ^ P[l].
    - We need, for each r, the max value of P[r] ^ P[l] over all valid l
      within the last K prefixes (sliding window of size K on l).
    - Maintain a Binary Trie (30-bit, since values fit under 2^30) holding
      the prefix XOR values currently in the window. Insert new prefix,
      evict the one that falls outside the window (old_index = r-K-1),
      then greedily walk the trie bit-by-bit (MSB to LSB) picking the
      opposite bit at each level when available to maximize the XOR —
      this is the standard "maximum XOR pair" trie query.
    - Track running max answer across all r.

Complexity:
    Time  : O(n * B)   where B = 30 (bit width) -> effectively O(n)
    Space : O(n * B)   worst case trie nodes (two arrays 'left'/'right' + cnt)
"""


# ------------------------- Solution ----------------------------------


from array import array
n, K = map(int, input().split())
w = list(map(int, input().split()))
P = [0] * (n + 1)
for i in range(1, n + 1):
    P[i] = P[i - 1] ^ w[i - 1]
left = array('i', [-1])
right = array('i', [-1])
cnt = array('i', [0])

def insert(x):
    node = 0
    cnt[node] += 1
    for bit in range(29, -1, -1):
        b = (x >> bit) & 1
        if b == 0:
            nxt = left[node]
            if nxt == -1:
                nxt = len(cnt)
                left[node] = nxt
                left.append(-1)
                right.append(-1)
                cnt.append(0)
            node = nxt
        else:
            nxt = right[node]
            if nxt == -1:
                nxt = len(cnt)
                right[node] = nxt
                left.append(-1)
                right.append(-1)
                cnt.append(0)
            node = nxt
        cnt[node] += 1

def remove(x):
    node = 0
    cnt[node] -= 1
    for bit in range(29, -1, -1):
        b = (x >> bit) & 1
        if b == 0:
            node = left[node]
        else:
            node = right[node]
        cnt[node] -= 1

def best_xor(x):
    node = 0
    result = 0
    for bit in range(29, -1, -1):
        b = (x >> bit) & 1
        if b == 0:
            nxt = right[node]
            if nxt != -1 and cnt[nxt] > 0:
                result |= (1 << bit)
                node = nxt
            else:
                node = left[node]
        else:
            nxt = left[node]
            if nxt != -1 and cnt[nxt] > 0:
                result |= (1 << bit)
                node = nxt
            else:
                node = right[node]
    return result
answer = 0
for r in range(1, n + 1):
    insert(P[r - 1])
    old_index = r - K - 1
    if old_index >= 0:
        remove(P[old_index])
    answer = max(answer, best_xor(P[r]))
print(answer)
