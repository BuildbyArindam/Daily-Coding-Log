"""
Problem: Creating Abbreviations
Platform: Codeforces
Link: https://codeforces.com/contest/2257/problem/A
Contest: Codeforces Round 1117 (Div. 2), Problem A
Date solved: 2026-08-18

Approach:
Track the set of "known" starting letters (from the n initial words).
An abbreviation can only be legally created if every letter it contains
already belongs to a word that starts with that letter — and once
created, it only contributes its own first letter as a new "known"
starting letter (the rest of the abbreviation is irrelevant going
forward, per the editorial's key observation). So repeatedly scan the
pending abbreviations, resolve any whose letters are all known, add
their first letters to the known set, and repeat until no more
abbreviations can be resolved. If all abbreviations get resolved -> YES,
else -> NO.

Time complexity: O(26 * m * L) per test case
  - The outer while loop runs at most 26 times (each pass must add at
    least one new letter to known_letters, and there are only 26
    possible letters, otherwise it breaks).
  - Each pass scans all still-pending tags (O(m)) and checks subset
    membership for a tag of length L (O(L)).

Space complexity: O(n + m + L) — storing known letters (O(26)) and the
list of abbreviations.
"""


# ----------------------- Solution -------------------------

import sys

def resolve_case(known_letters, pending_tags):
    still_waiting = list(pending_tags)
    while True:
        newly_built = []
        for tag in still_waiting:
            if set(tag) <= known_letters:
                newly_built.append(tag)
        if not newly_built:
            break
        built_set = set(newly_built)
        for tag in newly_built:
            known_letters.add(tag[0])
        still_waiting = [t for t in still_waiting if t not in built_set]
        if not still_waiting:
            break
    return len(still_waiting) == 0

def handle_single_case(reader):
    n_words, m_tags = map(int, reader.readline().split())
    base_letters = set()
    for _ in range(n_words):
        w = reader.readline().strip()
        base_letters.add(w[0].upper())
    abbrev_list = []
    for _ in range(m_tags):
        a = reader.readline().strip()
        abbrev_list.append(a)
    success = resolve_case(base_letters, abbrev_list)
    return "YES" if success else "NO"

def main():
    data_stream = sys.stdin
    total_cases = int(data_stream.readline())
    results = []
    for _ in range(total_cases):
        results.append(handle_single_case(data_stream))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
