"""
Problem: Battle of Words
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-12
Date Solved: 2026-09-09
Difficulty: Easy 
Topics: Strings, Simulation, Implementation, Hashing (character-to-value mapping)

Approach:
Split both strings into word lists, then compare word-by-word (zip pairs
them positionally). For each word, sum letter values (a=1..z=26), doubling
the value of any uppercase letter. Whoever's word has the higher score wins
that round; tally round wins for both sides and compare totals to decide
the overall winner.

Time Complexity:  O(n) - n = total number of characters across both strings
                   (each letter is visited once)
Space Complexity: O(w) - w = number of words (from the split() calls);
                   no extra space scales with letter count
"""


# ------------------------ Solution ------------------------------------


def battle(our_team, opponent):
    our_words = our_team.split()
    opponent_words = opponent.split()
    our_wins = 0
    opponent_wins = 0
    for our_word, opponent_word in zip(our_words, opponent_words):
        our_value = 0
        opponent_value = 0
        for letter in our_word:
            value = ord(letter.lower()) - ord('a') + 1
            if letter.isupper():
                value *= 2
            our_value += value
        for letter in opponent_word:
            value = ord(letter.lower()) - ord('a') + 1
            if letter.isupper():
                value *= 2
            opponent_value += value
        if our_value > opponent_value:
            our_wins += 1
        elif opponent_value > our_value:
            opponent_wins += 1
    if our_wins > opponent_wins:
        return "We win"
    elif our_wins < opponent_wins:
        return "We lose"
    else:
        return "Draw"
