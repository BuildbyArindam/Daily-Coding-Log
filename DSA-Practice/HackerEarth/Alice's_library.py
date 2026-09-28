"""
Problem   : Alice's library
Platform  : HackerEarth (Medium)
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/katrina-and-library-c2ed51f3/
Date      : 2026-09-28
Topics    : Data Structures, Stacks, Trees

Approach  : Treat '/' as opening a nested group and '\\' as closing it.
            Keep a stack of lists, one per open group. On '/', push a new
            empty list. On any other character, append it to the top list.
            On '\\', pop the top list, join and reverse it, then append the
            result to the enclosing group (or store it as the final answer
            if the stack is empty). Inner groups are reversed before the
            outer group reverses its contents.

Complexity: Time  - O(n * d) worst case, where d is the nesting depth, since
                    each level re-joins and reverses its contents (O(n) for
                    shallow nesting, O(n^2) for deeply nested input).
            Space - O(n) for the stack.
"""


# ------------------------------------- Solution --------------------------------------------------


s = input().strip()
stack = []
for ch in s:
    if ch == '/':
        stack.append([])
    elif ch == '\\':
        books = ''.join(stack.pop())[::-1]
        if stack:
            stack[-1].append(books)
        else:
            answer = books
    else:
        stack[-1].append(ch)
print(answer)
