/*
 * Problem   : 1729. Find Followers Count
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/find-followers-count/
 * Difficulty: Easy
 * Topics    : Database
 * Date      : 2026-10-08
 *
 * Approach:
 *   Each row in Followers is one (user_id, follower_id) pair, so the number
 *   of followers per user is the number of rows per user_id. Group by
 *   user_id, count follower_id, and sort by user_id ascending.
 *
 * Complexity:
 *   Time  : O(n log n) - one pass to group, plus sorting the grouped
 *           result (the sort is on distinct user_ids, so it is O(k log k)
 *           where k <= n).
 *   Space : O(k) - one aggregate row per distinct user_id.
 */


----------------------------------------------- Solution ---------------------------------------------------


-- # Write your MySQL query statement below
select user_id , count(follower_id) as 'followers_count'
from Followers
group by user_id
order by user_id asc
