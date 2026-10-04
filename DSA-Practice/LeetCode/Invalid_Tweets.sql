/*
 * Problem:    1683. Invalid Tweets
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/invalid-tweets/
 * Difficulty: Easy
 * Topics:     Database
 * Date:       2026-10-04
 *
 * Approach:
 *   A tweet is invalid when its content has more than 15 characters.
 *   Filter rows with CHAR_LENGTH(content) > 15 and return tweet_id.
 *   CHAR_LENGTH is used instead of LENGTH because LENGTH counts bytes,
 *   which differs from character count for multi-byte characters.
 *
 * Time Complexity:  O(n), one scan over the Tweets table
 * Space Complexity: O(1), no extra storage beyond the result set
 */


----------------------------------------- Solution -----------------------------------------------------------


-- # Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
