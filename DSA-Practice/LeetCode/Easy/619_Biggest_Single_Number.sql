/*
 * LeetCode 619. Biggest Single Number 
 * Link: https://leetcode.com/problems/biggest-single-number/
 * Difficulty: Easy
 * Topics: Database
 * Date: 2026-10-08
 *
 * Approach:
 *   1. Group rows by num and keep only values that appear exactly once.
 *   2. Sort those values in descending order and take the top one (LIMIT 1).
 *   3. Wrap the result in an outer aggregate so an empty set returns NULL
 *      instead of no rows.
 *
 * Time:  O(n log n)  (grouping + sorting)
 * Space: O(n)        (intermediate CTE results)
 */


------------------------------------------- Solution ------------------------------------------------------


-- # Write your MySQL query statement below
with cte as
(select num, (dense_rank() over(order by num)) as num_rank
from mynumbers),

cte2 as (select num, count(num_rank) as rank_count
from cte
group by num_rank,num
having count(num_rank) = 1
order by num desc
limit 1)

select case 
           when count(num) = 1 then num
           when count(num) = 0 then Null
       end as num
 from cte2
