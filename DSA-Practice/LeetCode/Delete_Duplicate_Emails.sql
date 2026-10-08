/*
 * Problem   : 196. Delete Duplicate Emails
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/delete-duplicate-emails/
 * Difficulty: Easy
 * Topics    : Database
 * Date      : 2026-10-08
 *
 * Approach  : Self-join Person with itself on Email. For every pair where
 *             p2.id > p1.id, p2 is a later duplicate of p1, so delete p2.
 *             This keeps only the row with the smallest id per email.
 *
 * Complexity: Time  - O(n^2) worst case for the nested-loop join, roughly
 *                     O(n) to O(n log n) if the optimizer uses an index on Email.
 *             Space - O(1) extra; the delete happens in place.
 */


--------------------------------------- Solution ------------------------------------------------------


-- # Write your MySQL query statement below
delete p2 from Person p1, Person p2
where p1.Email = p2.Email and p2.id > p1.id;
