/*
 * Problem   : 119. Pascal's Triangle II
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/pascals-triangle-ii/
 * Difficulty: Easy
 * Topics    : Array, Dynamic Programming
 * Date      : 2026-10-07
 *
 * Approach:
 *   Build the requested row directly using the binomial coefficient
 *   recurrence instead of generating all previous rows:
 *       C(n, i) = C(n, i-1) * (n - i + 1) / i
 *   Each element is derived from the one before it, starting at C(n, 0) = 1.
 *   Multiplication happens before division so the result is always an
 *   exact integer; a wider type guards against intermediate overflow.
 *
 * Complexity:
 *   Time : O(n)  - single pass over rowIndex + 1 elements
 *   Space: O(1)  - extra space, excluding the output vector
 *                  (O(n) including the returned row)
 */


// -------------------------------------------- Solution --------------------------------------------


class Solution {
public:
    vector<int> getRow(int rowIndex) {
        std::vector<int> result;

        // Initialize the first element of the row to 1.
        result.push_back(1);

        // Calculate each element in the row using the binomial coefficient formula.
        for (int i = 1; i <= rowIndex; i++) {
            long prevElement = result[i - 1];
            // Use the formula C(r, i) = C(r, i-1) * (r - i + 1) / i
            long currentElement = prevElement * (rowIndex - i + 1) / i;
            result.push_back(static_cast<int>(currentElement));
        }

        return result;
    }
};
