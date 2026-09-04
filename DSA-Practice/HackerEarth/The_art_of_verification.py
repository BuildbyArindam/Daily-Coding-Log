# Problem: The Art of Verification
# Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-art-of-verification/
# Date: 2026-09-04
# Platform: HackerEarth | Difficulty: Easy | Topic: Ad-Hoc, Open
#
# Approach:
#   Parse a query-string-style input (after the first '?') containing
#   key=value pairs for username, pwd, profile, role, key — but keys can
#   appear in ANY order and are '&'-joined. Locate each key's start position
#   with str.find, sort keys by position, then slice each value as the
#   substring between one key's start and the next key's start (trimming a
#   trailing '&' where needed, or taking the rest of the string for the last key).
#
# Time complexity:  O(n) — a handful of find() scans + one pass to slice values
# Space complexity: O(n) — dict/list proportional to input length


# ---------------------------- Solution ------------------------------------


name = input()                  # Reading input from STDIN
query = name.split('?', 1)[1]
keys = ["username", "pwd", "profile", "role", "key"]
values = {}
positions = []
for k in keys:
    pos = query.find(k + "=")
    positions.append((pos, k))
positions.sort()
for i in range(len(positions)):
    pos, k = positions[i]
    start = pos + len(k) + 1
    if i + 1 < len(positions):
        next_pos, _ = positions[i + 1]
        value = query[start:next_pos]
        if value.endswith("&"):
            value = value[:-1]
    else:
        value = query[start:]
    values[k] = value
print("username:", values["username"])
print("pwd:", values["pwd"])
print("profile:", values["profile"])
print("role:", values["role"])
print("key:", values["key"])
