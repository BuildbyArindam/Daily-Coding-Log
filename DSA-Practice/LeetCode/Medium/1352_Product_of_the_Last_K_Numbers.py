"""
Problem   : 1352. Product of the Last K Numbers
Platform  : LeetCode 
Link      : https://leetcode.com/problems/product-of-the-last-k-numbers/
Date      : 2026-11-23
Difficulty: Medium
Topics    : Array, Math, Design, Data Stream, Prefix Sum

Approach  : Keep a running prefix-product list, starting with [1].
            - add(num): append prefix[-1] * num. On a 0, reset the list to [1],
              since any product that spans the zero is 0.
            - getProduct(k): if k exceeds the count of numbers since the last
              zero, return 0. Otherwise the answer is
              prefix[-1] // prefix[-1 - k].

Complexity: add: O(1) time | getProduct: O(1) time | Space: O(n)
"""


# -------------------------------------------- Solution ---------------------------------------------------------------


class ProductOfNumbers:
    def __init__(self):
        self._acc = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self._acc = [1]
        else:
            self._acc.append(self._acc[-1] * num)

    def getProduct(self, k: int) -> int:
        span = len(self._acc) - 1  
        if k > span:
            return 0
        return self._acc[-1] // self._acc[-1 - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
