# Problem: Reverse Sentence
# Platform: FreeCodeCamp - Daily Coding Challenge
# Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-11
# Date Solved: 2026-09-05
# Difficulty: Easy
# Topics: String Manipulation, Arrays, Split/Join Operations
# 
# Approach: Split the sentence into words on whitespace, reverse the
# resulting list in place, then rejoin with single spaces to rebuild
# the sentence in reverse word order.
#
# Time Complexity: O(n) - n = number of characters in the sentence
# Space Complexity: O(n) - storage for the word list


# -------------------------- Solution -------------------------------


def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)
