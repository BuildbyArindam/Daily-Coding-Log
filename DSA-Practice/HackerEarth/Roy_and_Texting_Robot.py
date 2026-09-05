"""
Problem   : Roy and Texting Robot
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roy-and-texting-robot-2/
Difficulty: Easy
Topics    : Ad-Hoc, Algorithms, Approved, Basic Programming, Implementation, Open
Date      : 2026-09-05

Approach:
    Build a map from each character to (key number, press count) based on the
    9-key phone keypad layout. Walk through the string; each keypress costs
    presses[ch] time units, plus +1 extra if the current character's key
    differs from the previous character's key (simulating the "move to a new
    key" delay). Sum this over the string for each test case.

Time complexity : O(sum of len(s)) across all test cases — O(1) keypad setup.
Space complexity: O(1) extra (fixed-size keypad maps), O(1) per test case.
"""


# ---------------------------- Solution ------------------------------------


name = input() 
T = int(name)
keypad = {
    1: ".,?!1",
    2: "abc2",
    3: "def3",
    4: "ghi4",
    5: "jkl5",
    6: "mno6",
    7: "pqrs7",
    8: "tuv8",
    9: "wxyz9",
    0: "_0"
}
presses = {}
key = {}
for k, chars in keypad.items():
    for i, ch in enumerate(chars, 1):
        presses[ch] = i
        key[ch] = k
for _ in range(T):
    s = input().rstrip('\n')
    total_time = 0
    current_key = 1 
    for ch in s:
        new_key = key[ch]
        if new_key != current_key:
            total_time += 1
        total_time += presses[ch]
        current_key = new_key
    print(total_time)
