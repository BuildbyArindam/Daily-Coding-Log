"""
Problem   : The Best Internet Browser
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-best-internet-browser-3/
Difficulty: Easy
Topic     : Basic Programming / Implementation

Approach:
For each website string (format "www.<name>.com"), strip the fixed
"www." prefix and ".com" suffix to get the site name. Count the
consonants in that name; "Jhool count" = consonants + 4 (accounting
for the 4 fixed characters contributed by "www." and ".com" that are
themselves consonants/relevant characters per problem definition).
"Normal count" is simply the full length of the website string.
Print both counts as "jhool_count/normal_count" per test case.

Time Complexity : O(T * L) where T = number of test cases,
                   L = average length of website string
Space Complexity: O(1) extra space (excluding input storage)
"""


# ---------------------------- Solution -----------------------------


tc = int(input())
for _ in range(tc):
    website = input().strip()
    name = website[4:-4]
    consonants = 0
    for ch in name:
        if ch not in "aeiou":
            consonants += 1
    jhool_count = consonants + 4
    normal_count = len(website)
    print(str(jhool_count) + "/" + str(normal_count))
