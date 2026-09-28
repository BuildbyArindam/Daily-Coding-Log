"""
Problem   : Array Formation <Liv.ai>
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/circular-list-8e1319c9/
Difficulty: Easy
Topics    : Data Structures, Stacks, Queue, Sieve of Eratosthenes
Date      : 2026-09-28

Approach:
    Sieve all primes up to 10^6 once. Scan the array in order: primes go to a
    queue (FIFO, so original order is kept), non-primes go to a stack. Reverse
    the stack to get LIFO (pop) order, then print the queue followed by the stack.

Complexity:
    Time  : O(M log log M + N), where M = 10^6 (sieve) and N = len(A)
    Space : O(M + N)
"""


# ---------------------------------- Solution --------------------------------------------------


def queue_and_stack(A):
    MAX = 10**6
    is_prime = bytearray(b'\x01') * (MAX + 1)
    is_prime[0] = is_prime[1] = 0
    p = 2
    while p * p <= MAX:
        if is_prime[p]:
            start = p * p
            is_prime[start:MAX + 1:p] = b'\x00' * (((MAX - start) // p) + 1)
        p += 1
    queue = []
    stack = []
    for x in A:
        if is_prime[x]:
            queue.append(x)
        else:
            stack.append(x)
    stack.reverse()
    return queue, stack

n = int(input())
A = map(int, input().split())
out_ = queue_and_stack(A)
for i_out_ in out_:
    print(' '.join(map(str, i_out_)))
