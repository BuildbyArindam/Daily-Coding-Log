"""
Problem   : Quantum Chips (QUACHS)
Platform  : CodeChef — DSAMONDAY021
Link      : https://www.codechef.com/DSAMONDAY021/problems/QUACHS
Date      : 2026-09-21
Difficulty: Cakewalk/ Easy
Topics    : Basic Math, Basic I/O, Implementation

Approach:
Read three integers — lab_stock, extra_units, mishap_factor.
Total available chips = lab_stock + extra_units.
Each mishap destroys 2 units, so total lost = mishap_factor * 2.
Answer = total available - total lost.

Time complexity : O(1)
Space complexity: O(1)
"""


# --------------------------------------- Solution ------------------------------------------------


def compute_remaining():
    data = input().split()
    lab_stock, extra_units, mishap_factor = int(data[0]), int(data[1]), int(data[2])
    combined_total = lab_stock + extra_units
    lost_units = mishap_factor * 2
    final_count = combined_total - lost_units
    print(final_count)

if __name__ == "__main__":
    compute_remaining()
