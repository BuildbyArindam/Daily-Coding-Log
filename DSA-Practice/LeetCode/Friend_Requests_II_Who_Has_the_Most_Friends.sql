/*
 * Problem : 602. Friend Requests II: Who Has the Most Friends
 * Link    : https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
 * Platform: LeetCode
 * Difficulty: Medium
 * Topics  : Database
 * Date    : 2026-10-08
 *
 * Approach:
 *   A friendship is stored once as (requester_id, accepter_id), but it counts
 *   for both people. Count occurrences of each id as requester and as accepter
 *   separately, stack the two result sets with UNION ALL (not UNION, which would
 *   drop duplicate rows and undercount), then SUM per id and take the top one.
 *
 * Time Complexity : O(N log N) - two GROUP BY passes plus sorting the
 *                   aggregated ids for ORDER BY.
 * Space Complexity: O(U) - U = number of distinct user ids held in the
 *                   intermediate aggregates.
 */



------------------------------------------- Solution --------------------------------------------------


-- # Write your MySQL query statement below

select id , sum(cnt) as num from
(
  (select requester_id as id, count(*) as cnt from RequestAccepted group by requester_id)
union all
(select accepter_id as id, count(*) as cnt from RequestAccepted group by accepter_id) 
) t3
group by id
order by num desc limit 1
