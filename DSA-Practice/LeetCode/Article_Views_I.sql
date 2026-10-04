/*
 * Problem:    1148. Article Views I
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/article-views-i/
 * Difficulty: Easy
 * Topics:     Database
 * Date:       2026-10-04
 *
 * Approach:
 *   An author viewing their own article means author_id = viewer_id.
 *   Filter on that condition, use DISTINCT to drop duplicate authors
 *   (the Views table can contain repeated rows), and sort by id ascending.
 *
 * Time Complexity:  O(n log n) -- full scan + dedup + sort of matching rows
 * Space Complexity: O(k) -- k = number of distinct matching authors
 */


-------------------------------------------- Solution -------------------------------------------------------


-- # Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;
