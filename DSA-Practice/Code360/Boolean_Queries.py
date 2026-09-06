"""
Problem   : Boolean Queries
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/boolean-queries_2271421
Difficulty: Medium
Topics    : Design, Lazy Propagation, Versioning, Hashing
Date      : 2026-09-06

Approach:
Simulate an infinite boolean array without allocating it. Maintain a
`default_value` + a global `version` counter for O(1) "set all True/False"
operations. Each per-index write is stamped with the current version in a
dict. On read, an index's stored value is only valid if its stamped version
matches the current global version — otherwise it has been superseded by a
bulk set and falls back to `default_value`.

Time complexity : O(1) per operation (setAllTrue/False, setIndex*, getIndex)
Space complexity: O(k), where k = number of individually-set indices
"""


# -------------------------- Solution -------------------------------------


from typing import *

class InfiniteArray:
    def __init__(self):
        self.default_value = False
        self.version = 0
        self.values = {}

    def setAllTrue(self) -> None:
        self.default_value = True
        self.version += 1

    def setAllFalse(self) -> None:
        self.default_value = False
        self.version += 1

    def setIndexTrue(self, index: int) -> None:
        self.values[index] = (True, self.version)

    def setIndexFalse(self, index: int) -> None:
        self.values[index] = (False, self.version)

    def getIndex(self, index: int) -> bool:
        if index in self.values:
            value, value_version = self.values[index]
            if value_version == self.version:
                return value
        return self.default_value
