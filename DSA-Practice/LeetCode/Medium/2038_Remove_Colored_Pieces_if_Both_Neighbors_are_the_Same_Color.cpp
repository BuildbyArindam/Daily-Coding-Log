/*
 * Problem : 2038. Remove Colored Pieces if Both Neighbors are the Same Color
 * Platform: LeetCode
 * Link    : https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
 * Date    : 2026-10-05
 * Difficulty: Medium
 * Topics  : Math, String, Greedy, Game Theory
 *
 * Approach:
 *   A move never creates or destroys moves for the opponent, because Alice
 *   only removes 'A' pieces and Bob only 'B' pieces. So for each maximal run
 *   of k >= 3 identical letters, that player gets exactly (k - 2) moves.
 *   Sum the moves per player. Alice moves first, so she wins only if
 *   she has strictly more moves than Bob.
 *
 * Time : O(n), single pass over the string
 * Space: O(1)
 */


// ---------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    bool winnerOfGame(string colors) {
        int a=0;
        int b=0;
        for(int i=0;i<colors.size();)
        {
            char ch=colors[i];
            int count=0;
            while(i<colors.size())
            {
                if(colors[i]!=ch)break;
                i++;
                count++;
            }
            if(count>=3)
            {
                if(ch=='A')
                {
                    
                 a+=count-2;
                }
                else
                {
                    b+=count-2;
                }
            }
        }
        return a>b;
    }
};
