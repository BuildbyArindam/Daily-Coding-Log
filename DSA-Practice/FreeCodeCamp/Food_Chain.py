"""
Problem   : Food Chain
Platform  : FreeCodeCamp (Daily Coding Challenge, 08-02)
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/08-02
Date      : 2026-08-30

Approach:
    Build a predator -> prey mapping from the input pairs, and track
    which animals appear as prey. The apex predator is the one animal
    that never shows up as someone else's prey. Starting from the apex,
    walk the chain by repeatedly following predator -> prey links until
    an animal has no recorded prey, collecting the chain along the way.

Time Complexity : O(n)   -- one pass to build maps/sets, one pass to walk the chain
Space Complexity: O(n)   -- food_chain dict + prey_animals set + result list
"""


# ------------------------------- Solution ----------------------------------


def get_food_chain(pairs):
    food_chain = {}
    prey_animals = set()
    for predator, prey in pairs:
        food_chain[predator] = prey
        prey_animals.add(prey)
    apex = None
    for predator in food_chain:
        if predator not in prey_animals:
            apex = predator
            break
    chain = []
    while apex is not None:
        chain.append(apex)
        if apex in food_chain:
            apex = food_chain[apex]
        else:
            break
    return chain
