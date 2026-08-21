"""
Problem   : Round Table Killers
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/round-table-killers-b7b93156/
Difficulty: Easy
Topic     : Basic Programming / Implementation
Date      : 2026-08-21

Approach:
    Simulate the round-table elimination directly using a list of survivors.
    Track the current gunman's index; each turn he kills (gun_person % k)
    people starting from his immediate right. If the remaining survivors
    (excluding himself) are fewer than or equal to his kill count, he is
    the last one standing -> print him and stop. Otherwise remove the
    victims from the list (adjusting curr_idx when a removal happens
    before it), then pass the gun to the next survivor.

Time Complexity : O(n^2) worst case
                   (each pop() from a Python list is O(n); up to n
                    people can be removed over the course of the game)
Space Complexity: O(n) for the `people` list
"""


# ----------------------------- Solution --------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    x = int(input_data[2])
    people = list(range(1, n + 1))
    curr_idx = people.index(x)
    while True:
        gun_person = people[curr_idx]
        kills = gun_person % k
        if len(people) - 1 <= kills:
            print(gun_person)
            break
        for _ in range(kills):
            kill_idx = (curr_idx + 1) % len(people)
            people.pop(kill_idx)
            if kill_idx < curr_idx:
                curr_idx -= 1
        curr_idx = (curr_idx + 1) % len(people)

if __name__ == '__main__':
    solve()
