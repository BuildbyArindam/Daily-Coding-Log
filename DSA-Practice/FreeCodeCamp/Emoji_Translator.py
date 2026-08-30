"""
Problem: Emoji Translator
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-03
Date: 2026-08-30

Approach:
    Use a fixed emoji-to-word dictionary as a lookup table. Iterate over
    each character (emoji) in the input string, map it to its word via
    the dictionary, and join the resulting words with spaces.

Time Complexity: O(n)  -> n = number of emoji characters in the string,
                           each dict lookup is O(1) average case.
Space Complexity: O(1) extra -> the emoji_words dict is fixed-size/constant;
                           output string is O(n) but not counted as extra space.
"""


# ------------------------ Solution -----------------------------


def get_emoji_phrase(s):
    emoji_words = {
        "👶": "baby",
        "🐱": "cat",
        "🐕": "dog",
        "🐟": "fish",
        "🥵": "hot",
        "🧊": "ice",
        "🪨": "rock",
        "🦈": "shark",
        "🍲": "soup",
        "⭐": "star"
    }

    return " ".join(emoji_words[emoji] for emoji in s)
