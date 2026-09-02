# Problem: Unoccupied Computers
# Link: https://www.geeksforgeeks.org/problems/unoccupied-computers-1646661078/1
# Platform: GeeksforGeeks | Difficulty: Easy | Topic: Hash
# Date: 2026-09-02
#
# Approach: Simulate the login/logout stream with two sets — `active` for
# employees currently logged in, `rejected` for employees who were once
# denied login. For each character (employee) in s:
#   - if already active, they're logging out -> remove from active
#   - if already rejected once, ignore further attempts (already counted)
#   - else, if there's room (len(active) < n), log them in
#   - else, reject them and record in `rejected`
# Answer is the count of distinct employees ever rejected.
#
# Time Complexity: O(len(s)) — single pass, O(1) set operations
# Space Complexity: O(n) — active/rejected sets bounded by number of distinct employees


# --------------------------- Solution ------------------------------------


class Solution:
    def solve(self, n, s):
        # code here
        active = set() 
        rejected = set()
        for ch in s:
            if ch in active:
                active.remove(ch)
            elif ch in rejected:
                continue
            else:
                if len(active) < n:
                    active.add(ch)
                else:
                    rejected.add(ch)
        return len(rejected)
