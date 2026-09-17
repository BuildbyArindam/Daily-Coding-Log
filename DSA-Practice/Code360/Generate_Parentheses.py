'''
    Problem: Generate Parentheses (Print all combinations of balanced parentheses)
    Platform: Code360 (Naukri)
    Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380930
    Date: 2026-09-17
    Difficulty: Easy
    Topics: Recursion, Backtracking

    Approach:
        Build the string one character at a time via backtracking.
        Track counts of open and close brackets used so far.
        - Add '(' if open count < n
        - Add ')' only if close count < open count (ensures balance)
        Base case: when length == 2*n, the string is a valid combination.

    Time complexity: O(4^N / sqrt(N))   -- Catalan number growth
    Space complexity: O(4^N / sqrt(N))  -- to store/print all valid combinations
                        O(N) auxiliary recursion stack depth

    where N is the given number
'''


# -------------------------------- Solution ---------------------------------------------


'''
    Time complexity: O(4 ^ N / sqrt(N))
    Space complexity: O(4 ^ N / sqrt(N))

    where N is the given number
'''

def printParenthesesHelper(cur, opn, close, mx):
    if len(cur) == mx * 2:
        print(cur)
        return
    if opn < mx:
        printParenthesesHelper(cur + '{', opn + 1, close, mx)
    if close < opn:
        printParenthesesHelper(cur + '}', opn, close + 1, mx)

def printParantheses(n):
    strr = ""
    printParenthesesHelper(strr, 0, 0, n)
