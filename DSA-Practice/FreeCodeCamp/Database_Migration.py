"""
Problem: Database Migration
Platform: FreeCodeCamp (Daily Coding Challenge 07-03)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-03
Date Solved: 2026-08-31
Difficulty: Easy
Topic: Hashing, Dictionary Manipulation, Data Structures

Approach:
    Copy the input record, then walk through the schema's key-value pairs.
    For any schema key missing from the record, backfill it with the
    schema's default value. This "fills gaps without touching existing
    data" pattern is essentially a dict-merge with one-sided precedence
    (record wins over schema).

Time Complexity:  O(n) — n = number of keys in schema (single pass)
Space Complexity: O(n) — new dict `result` holds up to len(record) + len(schema) keys
"""


# ----------------------------- Solution -------------------------------------


def migrate_record(schema, record):
    result = record.copy()
    for key, value in schema.items():
        if key not in result:
            result[key] = value
    return result
