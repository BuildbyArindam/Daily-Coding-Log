"""
Problem   : Another String (ANOTSTR)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ANOTSTR
Date      : 2026-10-07
Difficulty: Easy
Topics    : Parity, Strings, Observation

Approach  : The answer depends only on the parity of the number of '1's in
            each string. Count the '1's in both strings and print YES if
            the parities match (even/even or odd/odd), otherwise NO.

Time      : O(N) per test case (str.count scans each string once),
            O(total input size) overall
Space     : O(total input size), since all input is read and tokenized up front
"""


# ------------------------------------------- Solution -----------------------------------------------------


import sys

def resolve_cases(raw_data):
    pointer = 0
    tokens = raw_data.split()
    total_tests = int(tokens[pointer]); pointer += 1
    results = []
    for _ in range(total_tests):
        _length = int(tokens[pointer]); pointer += 1  
        first_seq = tokens[pointer]; pointer += 1
        second_seq = tokens[pointer]; pointer += 1
        ones_first = first_seq.count('1')
        ones_second = second_seq.count('1')
        verdict = "YES" if (ones_first & 1) == (ones_second & 1) else "NO"
        results.append(verdict)
    return "\n".join(results)

def main():
    data = sys.stdin.read()
    sys.stdout.write(resolve_cases(data) + "\n")

if __name__ == "__main__":
    main()
