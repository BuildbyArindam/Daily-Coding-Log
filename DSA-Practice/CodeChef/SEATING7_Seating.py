"""
Platform  : CodeChef (START258B)
Problem   : Seating (SEATING7)
Link      : https://www.codechef.com/START258B/problems/SEATING7
Date      : 2026-09-30
Difficulty: Easy
Topics    : Hashing, Simulation, Two Pointers 

Approach:
    Store the M occupied seats in a hash set. Keep a single pointer that
    moves forward from seat 1, skipping occupied seats, and assign the
    next free seat to each of the K new people. The pointer never moves
    backward, so the scan is linear.

Complexity (per test case):
    Time  : O(M + K) average, since the pointer advances at most M + K times
    Space : O(M + K) for the set and the answer list
"""


# -------------------------------------- Solution ------------------------------------------


import sys

def resolve_seating():
    data = sys.stdin.read().split()
    ptr = 0
    total_cases = int(data[ptr]); ptr += 1
    results = []
    for _ in range(total_cases):
        n_val = int(data[ptr]); m_val = int(data[ptr+1]); k_val = int(data[ptr+2])
        ptr += 3
        taken = set()
        for _ in range(m_val):
            taken.add(int(data[ptr]))
            ptr += 1
        answers = []
        pointer_seat = 1
        for _ in range(k_val):
            while pointer_seat in taken:
                pointer_seat += 1
            taken.add(pointer_seat)
            answers.append(pointer_seat)
        results.append(" ".join(map(str, answers)))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    resolve_seating()
