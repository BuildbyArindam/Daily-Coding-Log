"""
Problem: Horoscope Match
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-12
Date Solved: 2026-09-02
Platform: FreeCodeCamp
Difficulty: Easy
Topics: Hashing, Dictionary Lookup, Array Indexing, Math

Approach:
Map each zodiac sign to its index in a fixed 12-sign list. Compute the
absolute index distance between the two signs, then fold it around the
circle by taking min(distance, 12 - distance), since compatibility is
symmetric in both directions around the zodiac wheel. Look up the folded
distance (0-6) in a precomputed compatibility percentage table.

Time Complexity: O(1) — signs list has fixed size 12, index() and dict
lookup are constant-time for fixed-size input.
Space Complexity: O(1) — fixed-size list and dict, no growth with input.
"""


# ------------------------- Solution ---------------------------------


def horoscope_match(sign1, sign2):
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer",
        "Leo", "Virgo", "Libra", "Scorpio",
        "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    compatibility = {
        0: "100%",
        1: "40%",
        2: "80%",
        3: "30%",
        4: "90%",
        5: "20%",
        6: "50%"
    }
    pos1 = signs.index(sign1)
    pos2 = signs.index(sign2)
    distance = abs(pos1 - pos2)
    distance = min(distance, 12 - distance)
    return compatibility[distance]
